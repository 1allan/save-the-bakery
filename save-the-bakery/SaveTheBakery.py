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
        self.player = Player('assets/spaceship.png', [self.screen.get_width() / 2, self.screen.get_height() * .8], (60, 80), 1)
        self.asteroids = []
        self.asteroid_tick = pygame.time.get_ticks()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.background.update(self.screen)
            self.generate_asteroids()
            self.player.update(self.screen)

            for a in self.asteroids:
                if a.rect.top < self.screen.get_height():
                    a.update(self.screen)
                else:
                    self.asteroids.remove(a)
        
                for b in self.player.bullets:
                    if b.rect.top < a.rect.top + a.height and a.rect.left < b.rect.left < a.rect.left + a.rect.width :
                        self.asteroids.remove(a)
                        self.player.bullets.remove(b)
            

            pygame.display.update()
    
    def generate_asteroids(self):
        now = pygame.time.get_ticks()

        if now - self.asteroid_tick > 400:
            self.asteroid_tick = now
            self.asteroids.append(Asteroid('assets/asteroid.png', [randint(-25 , self.screen.get_width()), -50], (50, 50)))

if __name__ == '__main__' :
    game = SaveTheBakery()
    game.start()