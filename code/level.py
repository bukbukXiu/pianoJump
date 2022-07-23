from typing import SupportsFloat
import pygame
from misc import import_individual_tiles
from settings import screen_height, layout, tile_size, note_tile_indices
from tiles import Tile

class Level:
    def __init__(self, layout, surface) -> None:
        self.display_surface = surface
        self.layout = layout
        self.key_sprites = self.create_tile_group(layout)

    def create_tile_group(self, layout):
        tile_list = import_individual_tiles('graphics/tiles/keys.png')
        sprite_group = pygame.sprite.Group()

        for index, note in enumerate(self.layout):
            x = index * tile_size
            y = screen_height - tile_size
            tile_index = note_tile_indices[note]
            tile_surface = tile_list[tile_index-1]
            sprite = Tile(x,y,tile_surface,note)
            sprite_group.add(sprite)
        return sprite_group

    def run(self):
        self.key_sprites.draw(self.display_surface)
