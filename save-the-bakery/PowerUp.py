import pygame
from random import choice

class PowerUp:
    
    def __init__(self, image_file, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.width, self.height = size
        self.type = choice([
            {'effect': 'one_more_bullet', 'modifier': 1}, 
            {'effect': 'bullet_speed', 'modifier': 10},
            {'effect': 'spaceship_speed', 'modifier': 3}
        ])


    def update(self, screen):
        self.rect.top += 1
        screen.blit(self.image, self.rect)