import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(image_file).convert()
        self.rect1 = self.image1.get_rect()
        self.rect1.left = 0
        self.rect1.top = 0
        self.width1 = self.image1.get_width() 
        self.height1 = self.image1.get_height() 

        self.image2 = pygame.image.load(image_file).convert()
        self.rect2 = self.image2.get_rect()
        self.rect2.left = 0
        self.rect2.top = -self.height1
        self.width2 = self.image2.get_width() 
        self.height2 = self.image2.get_height() 
        
    def update(self, screen):
        self.rect2.top += 1
        self.rect1.top += 1

        if self.rect1.top > screen.get_height() - 50:
            self.rect1.top = 0
            self.rect2.top = -self.height1
        
        screen.blit(self.image1, self.rect1)
        screen.blit(self.image2, self.rect2)
        