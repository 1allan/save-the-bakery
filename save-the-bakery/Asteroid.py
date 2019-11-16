import pygame

class Asteroid(pygame.sprite.Sprite):

    def __init__(self, image_file, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.size = size * 30
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.location = location
        self.rect.left, self.rect.top = self.location
        self.width, self.height = [self.size] * 2 
        self.duration = self.size / 30

    def update(self, screen):
        self.rect.top += 1
        screen.blit(self.image, self.rect)