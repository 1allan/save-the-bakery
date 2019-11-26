import pygame
from random import choice

from config import POWERUP_LIST, POWERUP_SIZE, POWERUP_IMAGE

class PowerUp:
    
    def __init__(self, position, size=POWERUP_SIZE,  image_file=POWERUP_IMAGE):
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.width, self.height = size
        self.type = choice(POWERUP_LIST)


    def update(self, screen):
        self.rect.top += 1
        screen.blit(self.image, self.rect)