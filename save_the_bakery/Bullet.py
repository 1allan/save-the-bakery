import pygame

from Entity import Entity
from config import BULLET_IMAGE

class Bullet(Entity): 

    def __init__(self, position, size, speed, shooter, direction=(1, 0), image_file=BULLET_IMAGE):
        super().__init__(position, size, image_file, convert_image=True)
        self.speed = speed
        self.direction = direction
        self.shooter = shooter

        self.rect.left -= self.width / 2
        self.rect.top -= self.height / 2 

    def update(self, screen):
        self.rect.top -= self.speed * self.direction[0]
        screen.blit(self.image, self.rect)