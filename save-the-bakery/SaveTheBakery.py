import pygame
from random import randint

from Background import Background
from Player import Player
from Asteroid import Asteroid

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
        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.background.update(self.screen)
            self.generate_asteroids()
            self.player.update(self.screen)
            self.collide()

            if self.player.life == 0:
                print(1)

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

    def collide(self):
        for a in self.asteroids:
            if a.rect.top < self.screen.get_height():
                a.update(self.screen)
            else:
                self.asteroids.remove(a)
    
            for b in self.player.bullets:
                if b.rect.top < a.rect.top + a.height and a.rect.left < b.rect.left < a.rect.left + a.rect.width :
                    
                    a.duration -= 1
                    if a.duration <= 0:
                        self.asteroids.remove(a)

                    self.player.bullets.remove(b)

            if a.rect.left < self.player.rect.left < a.rect.left + a.width and self.player.rect.top < a.rect.top + a.height:
                self.player.life -= 1

if __name__ == '__main__' :
    game = SaveTheBakery()
    game.start()