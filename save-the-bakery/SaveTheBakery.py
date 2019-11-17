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
            self.collide()

            if self.player.lifes == 0:
                print('Morreu')

            self.clock.tick(120)
            pygame.display.update()
    
    
    def generate_asteroids(self):
        now = pygame.time.get_ticks()
        if now - self.asteroid_tick > 800:
            self.asteroid_tick = now
            position = [randint(-25, self.screen.get_width()), -50]
            
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


    def collide(self):
        for a in self.asteroids:
            # if asteroid is out of screen
            if a.rect.top < self.screen.get_height():
                a.update(self.screen)
            else:
                self.asteroids.remove(a)
            
            p_y_max = self.player.rect.top
            p_y_min = self.player.rect.top + self.player.height
            p_x_min = self.player.rect.left
            p_x_max = self.player.rect.left + self.player.width
            player_hited = False
            
            #if player hits an asteroid
            if p_x_min <= a.rect.left <= p_x_max:
                if p_y_max <= a.rect.top <= p_y_min or p_y_max <= a.rect.top + a.rect.height <= p_y_min:
                    player_hited = True

            if p_x_min <= a.rect.left + a.width <= p_x_max:
                if p_y_max <= a.rect.top + a.height <= p_y_min or p_y_max <= a.rect.top <= p_y_min:
                    player_hited = True
            
            if player_hited:
                self.player.lifes -= 1               

            #if player catches a powerup
            for p in self.powerups:
                if p_x_min <= p.rect.left <= p_x_max:
                    if p_y_max <= p.rect.top <= p_y_min or p_y_max <= p.rect.top + p.rect.height <= p_y_min:
                        self.handle_powerup(p.type)
                        self.powerups.remove(p)
                        break
                        
                if p_x_min <= p.rect.left + p.width <= p_x_max:
                    if p_y_max <= p.rect.top + p.height <= p_y_min or p_y_max <= p.rect.top <= p_y_min:
                        self.handle_powerup(p.type)
                        self.powerups.remove(p)
                        break
            
            #if bullet hits an asteroid
            for i in range(len(self.player.bullets)):
                arr_bullets = self.player.bullets[i]
                asteroid_is_dead = False
                
                for b in arr_bullets:
                    if a.rect.top + a.height > b.rect.top > a.rect.top and a.rect.left < b.rect.left < a.rect.left + a.rect.width :        
                        a.duration -= 1
                        arr_bullets.remove(b)

                        if a.duration <= 0:
                            self.asteroids.remove(a)
                            asteroid_is_dead = True
                        
                        if asteroid_is_dead:
                            break

                if asteroid_is_dead:
                    break


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