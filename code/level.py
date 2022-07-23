from typing import SupportsFloat
import pygame
from misc import import_individual_tiles

class Level:
    def __init__(self, layout, surface) -> None:
        self.display_surface = surface
        self.layout = layout
        self.key_sprites = self.create_tile_group(layout)

    def create_tile_group(self, layout):
        tile_list = import_individual_tiles('graphics/tiles/keys.png')
        # sprite_group = pygame.sprite.Group()
        return tile_list


    def run(self):
        self.display_surface.blit(self.key_sprites[0],(0,0))