from typing import SupportsFloat
import pygame
from player import Player
from misc import import_individual_tiles
from settings import *
from tiles import Tile

class Level:
    def __init__(self, layout, surface) -> None:
        self.display_surface = surface
        
        # keys
        self.layout = layout
        self.key_sprites = self.create_tile_group(layout)

        # player
        self.player = self.player_setup(player_position) 

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

    def player_setup(self,position):
        player = pygame.sprite.GroupSingle()
        x = self.layout.index(position) * tile_size
        y = tile_size
        player.add(Player((x,y), self.display_surface))
        return player

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.key_sprites.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
        if player.on_ground and player.direction.y<0:
            player.on_ground = False

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * walk_speed
        

    def run(self):
        self.key_sprites.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.player.update()
        self.vertical_collision()
        self.horizontal_collision()