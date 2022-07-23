import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, x,y, surface, note) -> None:
        super().__init__()
        self.image = surface
        self.rect = self.image.get_rect(topleft = (x,y))
        self.note = note

