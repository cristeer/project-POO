import pygame
from random import choice
from mystery_laser import MysteryLaser
from sound import Sound
import os

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, offset: int, spaceship) -> None:
        super().__init__()
        
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.spaceship = spaceship
        self.mystery_sound = Sound().mystery_sound

        # Carregar imagem da nave misteriosa
        try:
            self.image = pygame.image.load('images/aliens/mystery.png')
        except:
            # Fallback se não encontrar a imagem
            self.image = pygame.Surface((60, 40))
            self.image.fill((255, 0, 255))  # Magenta
            
        self.rect = self.image.get_rect(topleft=(spaceship.rect.x, 140))

        self.mystery_health = 3
        self.mystery_kill = False
        
        # Sprites da Nave Misteriosa
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.mystery_ship_lasers_group = pygame.sprite.Group()

    def create_mystery_ship(self) -> None:
        self.mystery_ship_group.add(self)

    def mystery_shoot(self) -> None:
        if self.mystery_ship_group:
            position = self.mystery_ship_group.sprite.rect.center
            mystery_laser = MysteryLaser(position, -20, self.screen_height, self.spaceship.spaceship_group)
            self.mystery_ship_lasers_group.add(mystery_laser)
            self.mystery_sound.play()

    def update(self) -> None:
        if self.spaceship.spaceship_group.sprite:
            self.rect.x = self.spaceship.spaceship_group.sprite.rect.x - 20