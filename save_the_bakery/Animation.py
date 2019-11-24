import pygame

from config import ANIMATIONS

class Animation:

    def __init__(self, screen, name, position, velocity=60):
        self.screen = screen
        self.center = screen.get_width() / 2, screen.get_height() / 2
        self.last_tick = pygame.time.get_ticks()
        self.name = name
        self.velocity = velocity
        self.image = pygame.image.load(ANIMATIONS[self.name][0])
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.rect.center = [self.rect.left + self.image.get_width() / 2, self.rect.top + self.image.get_height() / 2] 
        self.frames = 0
        self.ended = False

    def change_image(self):
        if self.frames < len(ANIMATIONS[self.name]) - 1:
            self.frames += 1
        else:
            self.ended = True

        self.image = pygame.image.load(ANIMATIONS[self.name][self.frames])
        

    def update(self):
        now = pygame.time.get_ticks()
        
        if  now - self.last_tick  > self.velocity:
            self.last_tick = now
            self.change_image()
        
        self.screen.blit(self.image, self.rect.center)