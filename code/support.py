from os import walk
from pathlib import Path
import pygame
from csv import reader
from settings import tile_size


def import_sounds(path):
    sounds_list = {} 
    for _,_,snd_files in walk(path):
        for file in snd_files:
            if 'wav' in file:
                # sounds_list.append(file)
                sounds_list[Path(file).stem]= file 

    return sounds_list
    
def import_folder(self):
    pass