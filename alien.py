import pygame
from laser import Laser
from random import choice

class Alien(pygame.sprite.Sprite):

    def __init__(self, offset: int, alien_type: int = 1, x: int = None, y: int = 0):
        super().__init__()
        
        self.__alien_type = alien_type
        self.__offset = offset
        self.__aliens_direction = 1

        # Sprites
        self.__aliens_group = pygame.sprite.Group()
        self.__aliens_lasers_group = pygame.sprite.Group()
        
        # Carregar imagem do alien baseado no tipo
        self.__image = pygame.image.load(f'images/aliens/alien_{self.alien_type}.png')
        self.__rect = self.image.get_rect(topleft = (x or 0, y))

    # Setters e Getters
    @property
    def alien_type(self):
        return self.__alien_type

    @alien_type.setter
    def alien_type(self, value):
        self.__alien_type = value

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def aliens_direction(self):
        return self.__aliens_direction

    @aliens_direction.setter
    def aliens_direction(self, value):
        self.__aliens_direction = value

    @property
    def aliens_group(self):
        return self.__aliens_group

    @aliens_group.setter
    def aliens_group(self, value):
        self.__aliens_group = value

    @property
    def aliens_lasers_group(self):
        return self.__aliens_lasers_group

    @aliens_lasers_group.setter
    def aliens_lasers_group(self, value):
        self.__aliens_lasers_group = value

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
 
    def create_aliens(self, offset: int) -> None:
        self.aliens_group.empty()
        for row in range(7):
            for col in range(11):
                x = 505 + col * 55
                y = 220 + row * 55

                if row == 0 or row == 1:
                    alien_type = 3
                elif row > 1 and row < 6:
                    alien_type = 2
                else:
                    alien_type = 1
                    
                alien_inst = Alien(offset, alien_type, (x + offset/2), y)
                self.aliens_group.add(alien_inst)

    def move_aliens(self, offset: int) -> None:
        for alien in self.aliens_group:
            if alien.rect.right >= (1415 - offset):
                self.aliens_direction = -1
                self._move_aliens_down_(2)
                break
            elif alien.rect.left <= (485 + offset):
                self.aliens_direction = 1
                self._move_aliens_down_(2)
                break
    
    def _move_aliens_down_(self, distance: int) -> None:
        if self.aliens_group:
            for alien in self.aliens_group:
                alien.rect.y += distance

    def aliens_shoot(self, screen_height: int) -> None:
        if self.aliens_group:
            rand_alien = choice(self.aliens_group.sprites())
            laser_sprite = Laser(rand_alien.rect.center, -6, screen_height)
            self.aliens_lasers_group.add(laser_sprite)

    def update(self, direction: int) -> None:
        self.rect.x += direction

    def destroy_aliens(self):
        self.aliens_group.empty() # implementar no destrutor
        self.aliens_lasers_group.empty()
        self.aliens_direction = 1
