import pygame
from random import randint

from Background import Background
from Player import Player
from Asteroid import Asteroid
from PowerUp import PowerUp

class SaveTheBakery:
    
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((400, 600))
        self.background = Background('assets/background.jpg', [0, 0])
        self.player = Player(
            'assets/spaceship.png', 
            [self.screen.get_width() / 2, self.screen.get_height() * .8],
            (60, 80), 
            5,
            300
        )
        self.asteroids = []
        self.asteroid_tick = pygame.time.get_ticks()
        self.powerup_tick = pygame.time.get_ticks()
        self.powerups = []
        self.clock = pygame.time.Clock()

    
    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.background.update(self.screen)
            self.generate_asteroids()
            self.player.update(self.screen)
            self.generate_powerups()
            
            for a in self.asteroids:
                if a.rect.top < self.screen.get_height():
                     a.update(self.screen)
                else:
                     self.asteroids.remove(a)
                
                if self.collide(self.player, a):
                    if self.player.lifes > 0:
                        self.player.lifes -= 1
                    else:
                        print('DEAD')

                for i in range(len(self.player.bullets)):
                    arr_bullets = self.player.bullets[i]
                    current_a = a

                    for b in arr_bullets:
                        if self.collide(b, a):
                            self.asteroids.remove(a)
                            arr_bullets.remove(b)

                    if current_a not in self.asteroids:
                        break        

                for p in self.powerups:
                    if self.collide(self.player, p):
                        self.handle_powerup(p.type)
                        self.powerups.remove(p)            

            self.clock.tick(120)
            pygame.display.update()
    
    
    def generate_asteroids(self):
        now = pygame.time.get_ticks()
        if now - self.asteroid_tick > 800:
            self.asteroid_tick = now
            position = [randint(-25, self.screen.get_width()), -60]
            
            if len(self.asteroids) > 0:
                last_asteroid = self.asteroids[len(self.asteroids) - 2]

                while last_asteroid.rect.left > position[0] >  last_asteroid.rect.left + last_asteroid.width and last_asteroid.rect.top > 0:
                    position = [randint(-25, self.screen.get_width()), -50]

            self.asteroids.append(Asteroid('assets/asteroid.png', position, randint(1, 3)))


    def generate_powerups(self):
        now = pygame.time.get_ticks()
        if now - self.powerup_tick > 1800:
            self.powerup_tick = now

            position = [randint(0, self.screen.get_width()), -50] 
            self.powerups.append(PowerUp('assets/cake.png', position, (30, 30)))
        
        for p in self.powerups:
            p.update(self.screen)


    def collide(self, object1, object2):
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
        
        return False

    def handle_powerup(self, pw):
        if pw['effect'] == 'one_more_bullet' and len(self.player.bullets) < 3:
            self.player.bullets.append([])
        
        elif pw['effect'] == 'bullet_speed':
            self.player.fire_cadence -= 50
        
        elif pw['effect'] == 'spaceship_speed':
            self.player.speed += 2


if __name__ == '__main__' :
    game = SaveTheBakery()
    game.start()