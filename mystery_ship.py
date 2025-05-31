import pygame
from random import choice

class MysteryShip(pygame.sprite.Sprite):

    def __init__(self, screen_width:int, offset:int) -> None: # Inica nave especial
        
        super().__init__()
        
        self.screen_width = screen_width
        self.offset = offset
        self.image = pygame.image.load('images/aliens/mystery.png')
        self.x = choice([self.offset/2, self.screen_width + self.offset - self.image.get_width()])

        if self.x == 0:
            self.speed = 3
        else:
            self.speed = -3
        
        self.rect = self.image.get_rect(topleft = (self.x, 40))

    def update(self) -> None: # Atualiza as movimentações da nave especial
        self.rect.x += self.speed

        if self.rect.right >= self.screen_width + self.offset/2:
            self.speed = -3
        elif self.rect.left <= self.offset/2:
            self.speed = 3