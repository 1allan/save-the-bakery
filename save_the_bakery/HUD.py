import pygame

class HUD:

    def __init__(self, screen, player_lifes=3, powerups=0):
        self.screen = screen
        self.components = []
        self.powerup_image = pygame.image.load('assets/cake.png')
        self.powerup_image = pygame.transform.scale(self.powerup_image, (20, 20))
        self.life_image = pygame.image.load('assets/heart.png')
        self.life_image = pygame.transform.scale(self.life_image, (20, 20))
        self.player_lifes = player_lifes
        self.powerups = powerups

    
    def change(self, hp=False, powerups=False):
        if hp or hp == 0:
            self.player_lifes = hp
        
        if powerups or powerups == 0:
            self.powerups = powerups

    
    def update(self):
        if self.player_lifes > 0:
            for i in range(self.player_lifes):
                self.screen.blit(self.life_image, (self.screen.get_width() - 30 - 25 * i, self.screen.get_height() - 30))

        for i in range(self.powerups):
            self.screen.blit(self.powerup_image, (self.screen.get_width() - 30 - 25 * i, self.screen.get_height() - 60))