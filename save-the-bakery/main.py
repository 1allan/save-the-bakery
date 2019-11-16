import pygame
from Background import Background
from Player import Player

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((400, 600))
keys = pygame.key.get_pressed()
clock = pygame.time.Clock()

bg = Background('assets/background.jpg', [0, 0])
player = Player('assets/spaceship.png', [screen.get_width() / 2, screen.get_height() / 2], (60, 80), 1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    bg.update(screen)
    player.update(screen)
    screen.blit(player.image, player.rect)

    pygame.display.update()