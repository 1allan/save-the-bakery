import pygame
from random import randint

from Asteroid import Asteroid
from Bullet import Bullet

class DeathStar(Asteroid):

    def __init__(self, position):
        super().__init__(position, image_file='assets/deathstar.png')
        self.bullets = []
        self.rect.top = randint(self.height, 300)
        self.rect.left = -self.width
        self.fire_cadence = 800
        self.start_shooting = 1800
        self.last_shot = pygame.time.get_ticks()
    
    def update(self, screen):
        now = pygame.time.get_ticks()
        
        if now > self.start_shooting and now - self.last_shot > self.fire_cadence:
            self.last_shot = now

            self.bullets.append(Bullet(
                [self.rect.left + self.width / 2, self.rect.top + self.height / 2],
                (15, 40),
                8,
                DeathStar,
                -1
            ))

        self.rect.left += 1

        screen.blit(self.image, self.rect)