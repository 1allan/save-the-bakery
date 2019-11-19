import pygame

class Background(pygame.sprite.Sprite):
    
    def __init__(self, screen, image_file='assets/background.jpg', location=[0, 0]):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(image_file).convert()
        self.rect1 = self.image1.get_rect()
        self.rect1.left = 0
        self.rect1.top = 0
        self.width1 = self.image1.get_width() 
        self.height1 = self.image1.get_height() 

        self.image2 = pygame.image.load(image_file).convert()
        self.image2 = pygame.transform.scale(self.image2, (self.image1.get_width(), self.image1.get_height()))
        self.rect2 = self.image2.get_rect()
        self.rect2.left = 0
        self.rect2.top = -self.height1
        self.width2 = self.image2.get_width() 
        self.height2 = self.image2.get_height()

        self.screen = screen


    def update(self):
        self.rect2.top += 1
        self.rect1.top += 1

        if self.rect1.top >= self.screen.get_height():
            self.rect1.top = -self.height1
            
        if self.rect2.top >= self.screen.get_height():
            self.rect2.top = -self.height2
        
        self.screen.blit(self.image1, self.rect1)
        self.screen.blit(self.image2, self.rect2)
        