import pygame
from random import choice

from Entity import Entity
from config import POWERUP_LIST, POWERUP_SIZE, POWERUP_IMAGE

class PowerUp(Entity):
    
    def __init__(self, position, size=POWERUP_SIZE,  image_file=POWERUP_IMAGE):
        super().__init__(position, size, image_file)
        self.type = choice(POWERUP_LIST)


    def update(self, screen):
        self.rect.top += 1
        screen.blit(self.image, self.rect)