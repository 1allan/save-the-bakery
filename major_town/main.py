import pygame
from background import Background
from player import Player

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((400, 600))
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

bg = Background('assets/background.png', [0, 0])
player = Player('assets/spaceship.png', [screen.get_width() / 2, screen.get_height() / 2], (60, 80), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    screen.blit(bg.image, bg.rect)
    player.update(screen)
    screen.blit(player.image, player.rect)
    
    pygame.display.update()