import pygame

tile_size = 64
screen_width = 12 * tile_size
screen_height = 480

layout = 'aAbcCdDefFgG'
player_position = 'e'

walk_speed = 7
jump_speed = -15
gravity = 1

# lowercase indicates a sharp
note_tile_indices = {
    'a':4,
    'A':1,
    'b':3,
    'c':2,
    'C':1,
    'd':4,
    'D':1,
    'e':3,
    'f':2,
    'F':1,
    'g':4,
    'G':1
}