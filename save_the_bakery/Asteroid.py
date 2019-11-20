import pygame
from random import randint

from config import ASTEROID_SIZE_RANGE, ASTEROID_IMAGE

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, position, image_file=ASTEROID_IMAGE, size=ASTEROID_SIZE_RANGE):
        pygame.sprite.Sprite.__init__(self)
        self.size = randint(ASTEROID_SIZE_RANGE[0], ASTEROID_SIZE_RANGE[1]) * 30
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.left, self.rect.top = self.position
        self.width, self.height = [self.size] * 2
        self.center = (self.rect.left + self.width / 2, self.rect.top + self.height / 2)
        self.duration = size


    def update(self, screen):
        self.rect.top += 1
        screen.blit(self.image, self.rect)