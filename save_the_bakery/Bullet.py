import pygame

from config import BULLET_IMAGE

class Bullet: 

    def __init__(self, position, size, speed, shooter, direction=1, image_file=BULLET_IMAGE):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.width, self.height = size
        self.speed = speed
        self.direction = direction
        self.shooter = shooter

        self.rect.left -= self.width / 2
        self.rect.top -= self.height / 2 

    def update(self, screen):
        self.rect.top -= self.speed * self.direction
        screen.blit(self.image, self.rect)