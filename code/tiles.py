import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, note):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft = pos)
        self.note = note

    def update(self, shift):
        self.rect.x += shift

class Static_Tile(Tile):
    def __init__(self, pos, size, note, surface):
        super().__init__(pos, size, note)
        self.image = surface
        # self.image.fill('white')