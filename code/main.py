import pygame
import sys
from settings import *
from level import Level
from pygame import mixer

# Setup
pygame.init()
mixer.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
# layout = 'aAbcCdDefFgG'
level = Level(layout, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(pygame.image.load('../graphics/background.png').convert_alpha(), (0,0))
    level.run()
    pygame.display.update()
    clock.tick(60)

