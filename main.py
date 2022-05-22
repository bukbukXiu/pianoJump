import pygame
# from sys import exit
import sys
from settings import *
from tiles import Tile
from level import Level

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('red')
    level.run()

    pygame.display.update()
    clock.tick(60)

