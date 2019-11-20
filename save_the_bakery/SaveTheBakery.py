import pygame
from random import randint, choice

from config import (
    RESOLUTION, 
    CLOCK, 
    ASTEROID_GEN_INTERVAL, 
    SPECIAL_ASTEROIDS,
    POWERUP_GEN_INTERVAL,
    POWERUP_ON_KILL_CHANCE,
    PLAYER_MAX_BULLETS,
    PLAYER_MAX_SPEED,
    PLAYER_MAX_FIRE_CADENCE
)

from Background import Background
from Player import Player
from Asteroid import Asteroid
from PowerUp import PowerUp

class SaveTheBakery:
    
    def __init__(self):
        pygame.init()
        pygame.display.init()
        pygame.display.set_caption('Save The Bakery')
        self.clock = pygame.time.Clock()
        self.screen_width, self.screen_height = RESOLUTION
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.background = Background(screen=self.screen)
        self.player = Player(self.screen)
        self.asteroids = []
        self.powerups = []
        self.asteroid_tick = pygame.time.get_ticks()
        self.powerup_tick = pygame.time.get_ticks()

    def main(self):
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.background.update()
            self.player.update()
            self.generate_asteroids()
            self.generate_powerups()

            for a in self.asteroids:
                if a.rect.top < self.screen_height:
                    a.update(self.screen)
                else:
                    self.asteroids.remove(a)
                
                if self.collide(self.player, a):
                    if self.player.lifes > 0:
                        self.player.lifes -= 1
                    else:
                        print('DEAD')

                current_a = a
                for i in range(len(self.player.bullets)):
                    arr_bullets = self.player.bullets[i]

                    for b in arr_bullets:
                        if self.collide(b, a):
                            self.generate_powerups((a.rect.left, a.rect.top))
                            self.asteroids.remove(a)
                            arr_bullets.remove(b)

                    if current_a not in self.asteroids:
                        break        

                for p in self.powerups:
                    if self.collide(self.player, p):
                        self.handle_powerup(p.type)
                        self.powerups.remove(p)
                    
                    if p.rect.top > self.screen_height:
                        self.powerups.remove(p)            

            self.clock.tick(CLOCK)
            pygame.display.update()

    
    def collide(self, object1, object2) -> bool:
        if object1.width < object2.width:
           small, big = object1, object2
        else:
           small, big = object2, object1
        
        big_max_y = big.rect.top
        big_min_y = big.rect.top + big.height
        big_min_x = big.rect.left
        big_max_x = big.rect.left + big.width
        small_max_y = small.rect.top
        small_min_y = small.rect.top + small.height
        small_min_x = small.rect.left
        small_max_x = small.rect.left + small.width
            
        if big_min_x <= small_min_x <= big_max_x or big_min_x <= small_max_x <= big_max_x:
            return big_max_y <= small_max_y <= big_min_y or big_max_y <= small_min_y <= big_min_y
    
    def generate_asteroids(self):
        now = pygame.time.get_ticks()
        if now - self.asteroid_tick > ASTEROID_GEN_INTERVAL:
            self.asteroid_tick = now
            position = [randint(0, self.screen_width), -60]
            
            if len(self.asteroids) > 0:
                last_asteroid = self.asteroids[len(self.asteroids) - 2]

                while (
                    last_asteroid.rect.left > position[0] > 
                    last_asteroid.rect.left + last_asteroid.width and last_asteroid.rect.top > 0
                ):
                    position = [randint(0, self.screen_width), -60]
            
            sp_asteroid = choice(SPECIAL_ASTEROIDS)
            if randint(0, 100) < sp_asteroid['chance']:
                self.asteroids.append(sp_asteroid['class'](position))
            else:
                self.asteroids.append(Asteroid(position))

    def generate_powerups(self, asteroid_pos=False):
        if not asteroid_pos and POWERUP_GEN_INTERVAL > 0:
            now = pygame.time.get_ticks()

            if now - self.powerup_tick > POWERUP_GEN_INTERVAL:
                
                self.powerup_tick = now
                position = [randint(0, self.screen_width), -50] 
                self.powerups.append(PowerUp(position))
        
        elif asteroid_pos and randint(0, 100) < POWERUP_ON_KILL_CHANCE:
            self.powerups.append(PowerUp(asteroid_pos))

        for p in self.powerups:
            p.update(self.screen)


    def handle_powerup(self, pw):
        if pw['effect'] == 'one_more_bullet' and len(self.player.bullets) < PLAYER_MAX_BULLETS:
            self.player.bullets = [[]] * pw['modifier']
        
        elif pw['effect'] == 'fire_cadence' and self.player.fire_cadence > PLAYER_MAX_FIRE_CADENCE:
            self.player.fire_cadence -= pw['modifier']
        
        elif pw['effect'] == 'spaceship_speed' and self.player.speed < PLAYER_MAX_SPEED:
            self.player.speed += pw['modifier']