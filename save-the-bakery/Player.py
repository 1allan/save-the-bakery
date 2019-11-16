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
        self.bullets = []
        self.fire_cadence = fire_cadence
        self.last_shot = pygame.time.get_ticks()
        self.life = 3

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

            b = Bullet(
                './assets/bullet.png', 
                [self.rect.left + self.width / 2, self.rect.top + self.height / 2], 
                [15, 60],
                30
            )

            self.bullets.append(b)     
    
    def update(self, screen):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_SPACE]:
            self.shoot(screen)
        
        for b in self.bullets:
 
            if b.rect.top < 0 :
                self.bullets.remove(b) 
 
            b.update(screen)
        
        self.move(screen, keys)
        screen.blit(self.image, self.rect)