import pygame
from random import randint

from config import DEATHSTAR_FIRE_CADENCE, DEATHSTAR_START_SHOOTING

from Asteroid import Asteroid
from Bullet import Bullet

class DeathStar(Asteroid):

    def __init__(self, position):
        super().__init__(position, image_file='assets/deathstar.png')
        self.bullets = []
        self.rect.top = randint(self.height, 300)
        self.rect.left = -self.width
        self.fire_cadence = DEATHSTAR_FIRE_CADENCE
        self.start_shooting = DEATHSTAR_START_SHOOTING
        self.last_shot = pygame.time.get_ticks()
    
    def update(self, screen):
        now = pygame.time.get_ticks()
        
        if now > self.start_shooting and now - self.last_shot > self.fire_cadence:
            self.last_shot = now

            self.bullets.append(Bullet(
                [self.rect.left + self.width / 2, self.rect.top + self.height / 2],
                (10, 60),
                8,
                DeathStar,
                (-1, 1),
                'assets/enemybullet.png'
            ))

        self.rect.left += 1

        screen.blit(self.image, self.rect)