import pygame

class Entity:

    def __init__(self, position, size, image_file, convert_image=False):
        self.position = position
        self.size = size
        self.width, self.height = self.size
        self.image = pygame.image.load(image_file).convert() if convert_image else pygame.image.load(image_file) 
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position
        self.rect.center = self.position