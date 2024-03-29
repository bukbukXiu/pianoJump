import pygame
from settings import jump_speed, gravity

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface) -> None:
        super().__init__()
        self.image = pygame.image.load('../graphics/character/small_finger.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = pos)
        # self.middlerect = pygame.Rect(bottomleft = pos + (self.image.get_width() / 2, 0),)
        self.middlerect = pygame.Rect(self.rect.left + self.rect.width / 2, self.rect.top, 1, self.rect.height)
        self.direction = pygame.math.Vector2(0,0)
        self.on_ground = False
        self.facing_rigth = False

    def get_input(self):
        keys = pygame.key.get_pressed()
        image = pygame.image.load('../graphics/character/small_finger.png').convert_alpha()
        flipped_image = pygame.transform.flip(image, True, False)
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_rigth = True
            self.image = flipped_image 
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_rigth = False
            self.image = image 
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()

    def apply_gravity(self):
        self.direction.y += gravity
        self.rect.y += self.direction.y
        self.middlerect.y += self.direction.y

    def jump(self):
        if self.on_ground: 
            self.direction.y = jump_speed

    def update(self):
        self.get_input()
