import pygame
from random import choice
from mystery_laser import MysteryLaser
from sound import Sound
import os

class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width: int, screen_height: int, offset: int, spaceship, sound) -> None:
        super().__init__()
        
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__offset = offset
        self.__spaceship = spaceship
        self.__mystery_sound = sound.mystery_sound

        # Carregar imagem da nave misteriosa
        self.__image = pygame.image.load('images/aliens/mystery.png')    
        self.__rect = self.image.get_rect(topleft=(spaceship.rect.x, 140))

        self.__mystery_health = 3
        self.__mystery_kill = False
        
        # Sprites da Nave Misteriosa
        self.__mystery_ship_group = pygame.sprite.GroupSingle()
        self.__mystery_ship_lasers_group = pygame.sprite.Group()

    # Setters e Getters
    @property
    def screen_width(self):
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, value):
        self.__screen_width = value

    @property
    def screen_height(self):
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, value):
        self.__screen_height = value

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def spaceship(self):
        return self.__spaceship

    @spaceship.setter
    def spaceship(self, value):
        self.__spaceship = value

    @property
    def mystery_sound(self):
        return self.__mystery_sound

    @mystery_sound.setter
    def mystery_sound(self, value):
        self.__mystery_sound = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value

    @property
    def rect(self):
        return self.__rect

    @rect.setter
    def rect(self, value):
        self.__rect = value

    @property
    def mystery_health(self):
        return self.__mystery_health

    @mystery_health.setter
    def mystery_health(self, value):
        self.__mystery_health = value

    @property
    def mystery_kill(self):
        return self.__mystery_kill

    @mystery_kill.setter
    def mystery_kill(self, value):
        self.__mystery_kill = value

    @property
    def mystery_ship_group(self):
        return self.__mystery_ship_group

    @mystery_ship_group.setter
    def mystery_ship_group(self, value):
        self.__mystery_ship_group = value

    @property
    def mystery_ship_lasers_group(self):
        return self.__mystery_ship_lasers_group

    @mystery_ship_lasers_group.setter
    def mystery_ship_lasers_group(self, value):
        self.__mystery_ship_lasers_group = value

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