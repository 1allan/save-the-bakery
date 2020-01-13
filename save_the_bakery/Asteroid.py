import pygame
from random import randint

from Entity import Entity
from config import ASTEROID_SIZE_RANGE, ASTEROID_IMAGE, ASTEROID_SPEED_RANGE

class Asteroid(Entity):

    def __init__(self, position, speed=ASTEROID_SPEED_RANGE, image_file=ASTEROID_IMAGE):
        self.size = randint(ASTEROID_SIZE_RANGE[0], ASTEROID_SIZE_RANGE[1]) * 30
        super().__init__(position, (self.size, self.size), image_file)
        self.speed = randint(speed[0], speed[1])
        self.hp = self.size[0] / 30
        
    def update(self, screen):
        self.rect.top += self.speed
        screen.blit(self.image, self.rect)