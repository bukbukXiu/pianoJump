from os import walk
from pathlib import Path
import pygame

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
    
print(import_sounds('sounds/'))