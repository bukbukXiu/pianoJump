import pygame
from settings import jump_speed, gravity

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface) -> None:
        super().__init__()
        self.image = pygame.image.load('graphics/character/small_finger.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        self.direction = pygame.math.Vector2(0,0)
        self.on_ground = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_rigth = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_rigth = False
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def apply_gravity(self):
        self.direction.y += gravity
        self.rect.y += self.direction.y


    def jump(self):
        if self.on_ground: 
            self.direction.y = jump_speed

    def update(self):
        self.get_input()
