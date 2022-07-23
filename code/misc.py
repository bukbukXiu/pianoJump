import pygame
from settings import tile_size
from os import walk
from pathlib import Path

def import_individual_tiles(path):
    surface = pygame.image.load('graphics/tiles/keys.png').convert_alpha()
    tiles_num = int(surface.get_width() / tile_size)
    tiles_list = []

    for col in range(tiles_num):
        tile_surface = pygame.Surface((tile_size,tile_size))
        tile_surface.blit(surface, (0,0), pygame.Rect(col*tile_size, 0, tile_size, tile_size))
        tiles_list.append(tile_surface)

    return tiles_list

def import_sounds(path):
    sounds_dict = {}
    for _,_,snd_files in walk(path):
        for file in snd_files:
            if 'wav' in file:
                dict_key = Path(file).stem
                sounds_dict[dict_key] = path + file
    return sounds_dict