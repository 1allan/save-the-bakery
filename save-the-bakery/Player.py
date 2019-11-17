import pygame

from Bullet import Bullet

class Player:

    def __init__(self, image_file, location, size, speed, fire_cadence):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.width, self.height = size
        self.speed = speed
        self.bullets = [[]]
        self.fire_cadence = fire_cadence
        self.last_shot = pygame.time.get_ticks()
        self.lifes = 3


    def move(self, screen, keys):
        if keys[pygame.K_w] and self.rect.top > -self.height / 2:
            self.rect.top -= self.speed
        if keys[pygame.K_s] and self.rect.top < screen.get_height() - self.height / 2:
            self.rect.top += self.speed
        if keys[pygame.K_a] and self.rect.left > -self.width / 2:
            self.rect.left -= self.speed
        if keys[pygame.K_d] and self.rect.left < screen.get_width() - self.width / 2:
            self.rect.left += self.speed


    def shoot(self, screen):
        now = pygame.time.get_ticks()
        
        if now - self.last_shot > self.fire_cadence:
            self.last_shot = now
            
            bullet_x_pos = [
                [self.rect.left + self.width / 2], 
                [self.rect.left + 20, self.rect.left + self.width - 20], 
                [self.rect.left + 5, self.rect.left + self.width / 2, self.rect.left + self.width - 5]
            ]
            
            bullet_y_pos = self.rect.top + self.height / 2

            for i in range(1, len(self.bullets) + 1):
                if len(self.bullets) == 3 and i == 2:
                    bullet_y_pos -= 50
                elif i == 3:
                    bullet_y_pos += 50
            
                b = Bullet(
                    './assets/bullet.png', 
                    [bullet_x_pos[len(self.bullets) - 1][i - 1], bullet_y_pos], 
                    [15, 60],
                    10
                )
                self.bullets[i - 1].append(b)

    
    
    def update(self, screen):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.shoot(screen)
        
        for i in range(len(self.bullets)):
            for b in self.bullets[i]:
                if b.rect.top < 0 :
                    self.bullets[i].remove(b) 
    
                b.update(screen)
        
        self.move(screen, keys)
        screen.blit(self.image, self.rect)