from os import walk
from pathlib import Path
import pygame
from csv import reader
from settings import tile_size

def import_folder(path):
    surface_list = [] 
    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
        
    return surface_list

def import_sounds(path):
    sounds_list = {} 
    for _,_,snd_files in walk(path):
        for file in snd_files:
            if 'wav' in file:
                # sounds_list.append(file)
                sounds_list[Path(file).stem]= file 

    return sounds_list
    
def import_csv_layout(path):
    keys_map = []
    with open(path) as map:
        level = reader(map,delimiter=',')
        for row in level:
            keys_map.append(list(row))
    return keys_map

def import_graphics(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / tile_size)
    tile_num_y = int(surface.get_size()[1] / tile_size)

    cut_tiles=[]
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = tile_num_x * tile_size
            y = tile_num_y * tile_size
            new_surf = pygame.Surface(size=(tile_size, tile_size))
            new_surf.blit(surface,(0,0),pygame.Rect(x,y,tile_size,tile_size))
            cut_tiles.append(new_surf)
    return cut_tiles