import pygame
from random import choice
from spaceship import Spaceship
from random import randint
class MysteryShip(pygame.sprite.Sprite):

    def __init__(self, screen_width:int, offset:int, spaceship:Spaceship) -> None: # Inica nave especial
        
        super().__init__()
        
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load('images/aliens/mystery.png')
        self.spaceship = spaceship

        # if self.x == 0:
        #     self.speed = 3
        # else:
        #     self.speed = -3
        
        self.rect = self.image.get_rect(topleft = (self.spaceship.sprite.rect.x, 140))

    def update(self) -> None: # Atualiza as movimentações da nave especial
        self.rect.x = self.spaceship.sprite.rect.x - 20
        # if self.rect.right >= self.screen_width + self.offset/2:
        #     self.speed = -3
        # elif self.rect.left <= self.offset/2:
        #     self.speed = 3