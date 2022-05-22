import pygame
from tiles import Tile
from player import Player
from settings import tile_size

class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if cell != ' ':
                    if cell == 'w':
                        color = 'white'
                        tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, color)
                        self.tiles.add(tile)
                    elif cell == 'b':
                        color = 'black'
                        tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, color)
                        self.tiles.add(tile)
                    elif cell == 'p':
                        self.player.add(Player((col_index * tile_size, row_index * tile_size)))



            

    def run(self):

        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        #player
        self.player.update()
        self.player.draw(self.display_surface)