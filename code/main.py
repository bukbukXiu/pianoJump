from ast import Load
from json import load
import pygame
# from sys import exit
import sys
from settings import *
from tiles import Tile
from level import Level
from level_data import level_0

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level_0,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('red')
    level.run()
    # test_surf = pygame.Surface(size=(tile_size, tile_size)
    # test_surf = pygame.Image.Load(
    # screen.blit(surface=test_surf)
    pygame.display.update()
    clock.tick(60)

