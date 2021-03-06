import pygame

from config import (
    PLAYER_IMAGE,
    PLAYER_SIZE, 
    PLAYER_HP, 
    PLAYER_POSITION, 
    PLAYER_SPEED,
    PLAYER_FIRE_CADENCE,
    PLAYER_BULLET_LINES,
    PLAYER_BULLET_SPEED,
    PLAYER_BULLET_SIZE
)

from Entity import Entity
from Bullet import Bullet

class Player(Entity):

    def __init__(self, screen, position=PLAYER_POSITION, size=PLAYER_SIZE, speed=PLAYER_SPEED, fire_cadence=PLAYER_FIRE_CADENCE, image_file=PLAYER_IMAGE):
        super().__init__(position, size, image_file)
        self.screen = screen
        self.speed = speed
        self.bullets = []
        self.powerups = []
        self.bullet_lines = PLAYER_BULLET_LINES
        self.fire_cadence = fire_cadence
        self.last_shot = pygame.time.get_ticks()
        self.hp = PLAYER_HP
        self.last_damage = pygame.time.get_ticks()
        self.invencible = False


    def move(self, keys):
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.rect.top > -self.height / 2:
            self.rect.top -= self.speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.rect.top < self.screen.get_height() - self.height / 2:
            self.rect.top += self.speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.rect.left > -self.width / 2:
            self.rect.left -= self.speed
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.rect.left < self.screen.get_width() - self.width / 2:
            self.rect.left += self.speed


    def shoot(self):
        now = pygame.time.get_ticks()
        
        if now - self.last_shot > self.fire_cadence:
            self.last_shot = now
            
            bullet_x_pos = [
                [self.rect.left + self.width / 2], 
                [self.rect.left + 20, self.rect.left + self.width - 20], 
                [self.rect.left + 5, self.rect.left + self.width / 2, self.rect.left + self.width - 5]
            ]
            
            bullet_y_pos = self.rect.top + self.height / 2

            for i in range(self.bullet_lines):
                if self.bullet_lines == 3:
                    if i == 1:
                        bullet_y_pos -= 30
                    else:
                        bullet_y_pos += 30
            
                b = Bullet(
                    [bullet_x_pos[self.bullet_lines - 1][i], bullet_y_pos], 
                    PLAYER_BULLET_SIZE,
                    PLAYER_BULLET_SPEED,
                    Player
                )
                self.bullets.append(b)

    
    def handle_hp(self, quantity=-1) -> int:
        now = pygame.time.get_ticks()

        if quantity < 0:
            if now - self.last_damage > 1000 or self.hp == PLAYER_HP:
                self.last_damage = now
                self.hp += quantity
                self.invencible = True
        else:
            self.hp += quantity
        
        return self.hp

    
    def update(self):
        now = pygame.time.get_ticks()
        image = self.image
        rect = self.rect

        if self.invencible and now - self.last_damage < 1000:
            image = pygame.image.load('assets/spaceshipdamaged.png')
            image = pygame.transform.scale(image, self.size)
            rect = image.get_rect()
        
        self.screen.blit(image, (self.rect.left, self.rect.top))