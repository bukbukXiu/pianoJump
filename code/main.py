from ast import Load
from json import load
import pygame
# from sys import exit
import sys

# Setup
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('red')
    level.run()
    pygame.display.update()
    clock.tick(60)

