import pygame
from laser import Laser
from random import choice
import os

class Alien(pygame.sprite.Sprite):
    def __init__(self, offset: int, alien_type: int = None, x: int = None, y: int = 0):
        super().__init__()
      
        self.alien_type = alien_type
        self.offset = offset
        self.aliens_direction = 1
        
        # Sprites
        self.aliens_group = pygame.sprite.Group()
        self.aliens_lasers_group = pygame.sprite.Group()
        
        # Carregar imagem do alien baseado no tipo
        if alien_type:
            try:
                self.image = pygame.image.load(f'images/aliens/alien_{self.alien_type}.png')
            except:
                # Fallback se não encontrar a imagem
                colors = {1: (255, 0, 0), 2: (0, 0, 255), 3: (255, 255, 255)}
                self.image = pygame.Surface((40, 30))
                self.image.fill(colors.get(self.alien_type, (255, 0, 0)))
        else:
            self.image = pygame.Surface((40, 30))
            self.image.fill((255, 0, 0))
            
        self.rect = self.image.get_rect(topleft=(x or 0, y))
    
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