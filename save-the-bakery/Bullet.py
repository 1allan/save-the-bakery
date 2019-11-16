import pygame

class Bullet: 

    def __init__(self, image_file, location, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert()
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.width, self.height = size

        self.rect.left -= self.width / 2
        self.rect.top -= self.height / 2 

    def update(self, screen):
        self.rect.top -= 1
        screen.blit(self.image, self.rect)