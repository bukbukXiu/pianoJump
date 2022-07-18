from re import X
import pygame
from support import import_sounds
from tiles import Tile, Static_Tile
from player import Player
from settings import tile_size, screen_width
from pygame import mixer
from support import import_csv_layout, import_graphics

class Level:
    def __init__(self, level_data, surface):
        # level setup
        self.display_surface = surface
        keys_layout = import_csv_layout(level_data['keys'])
        self.keys_sprites = self.create_tile_group(keys_layout,'keys')
        # print(self.keys_layout)
        # self.setup_level(level_data)
        self.setup_sound()
        self.world_shift = 0
        self.shift_threshold = screen_width // 6
        self.current_x = 0
        self.scale = 'abcdefg'

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for row_index, row in enumerate(layout):
            for col_index, col in enumerate(row):
                if col != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    if type == 'keys':
                        keys_tiles_list = import_graphics('graphics/tiles/keys.png')
                        tile_surf = keys_tiles_list[int(col)]
                        # new_surf = pygame.Surface((tile_size, tile_size))
                        # new_surf.fill('white')
                        self.display_surface.blit(new_surf,(0,0))

                        sprite = Static_Tile((x,y), tile_size, 'c',tile_surf)
                        sprite.image = tile_surf
                        sprite_group.add(sprite)

        return sprite_group

    def setup_sound(self):
        mixer.init() 

    # def setup_level(self, layout):
    #     self.tiles = pygame.sprite.Group()
    #     self.player = pygame.sprite.GroupSingle()
    #     self.sounds = import_sounds('sounds/')
    #     for row_index, row in enumerate(layout):
    #         for col_index, cell in enumerate(row):
    #             if cell != ' ':
                    # if cell == 'w':
                    #     color = 'white'
                    #     tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, color, 'white')
                    #     self.tiles.add(tile)
                    # elif cell == 'b':
                    #     color = 'black'
                    #     tile = Tile((col_index * tile_size, row_index * tile_size), tile_size, color, 'black')
                    #     self.tiles.add(tile)
                    # if cell == 'p':
                    #     self.player.add(Player((col_index * tile_size, row_index * tile_size)))
                    # else:
                    #     tile = Tile((col_index*tile_size, row_index*tile_size), tile_size, cell)
                    #     if cell == cell.lower():
                    #         tile.image.fill('white')
                    #     else:
                    #         tile.image.fill('black')
                    #     self.tiles.add(tile)


    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        
        if player_x < self.shift_threshold and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - self.shift_threshold and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8
            
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    # print(player.rect.bottom, " ", sprite.rect.top)
                    # sprite.image.fill('black')
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.on_left = True
                        self.cuttent_x = player.rect.left
                    if player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.on_right = True
                        self.cuttent_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >=0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <=0):
            player.on_right = False


    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    if player.on_ground == False:
                        print(sprite.note)
                        mixer.music.load('sounds/' + self.sounds[sprite.note])
                        mixer.music.play()
                    player.rect.bottom = sprite.rect.top 
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
        # replace gravity check with something more explicit
        if player.on_ground and (player.direction.y < 0 or player.direction.y > player.gravity):
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def run(self):

        #level tiles
        # self.keys_sprites.update(self.world_shift)
        self.keys_sprites.draw(self.display_surface)
        # self.scroll_x()

        #player
        # self.player.update()
        # self.vertical_movement_collision()
        # self.horizontal_movement_collision()
        # self.player.draw(self.display_surface)