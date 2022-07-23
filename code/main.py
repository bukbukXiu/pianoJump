import imp
import pygame
import sys
from settings import *
from level import Level

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
layout = 'aAbcCdDefFgG'
level = Level(layout, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()
    pygame.display.update()
    clock.tick(60)

