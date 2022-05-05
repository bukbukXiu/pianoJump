import pygame
from sys import exit

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = 


pygame.init()
screen = pygame.display.set_mode((384*2,215*2 ))
pygame.display.set_caption("Piano Jump")
clock = pygame.time.Clock()
# game_active = True

#define assets
sky_surf = pygame.image.load('assets/plx-5.png').convert_alpha()
sky_surf = pygame.transform.scale2x(sky_surf)



# main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    screen.blit(sky_surf, (0,0))

    pygame.display.update()
    clock.tick(60)