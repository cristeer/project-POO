import pygame
from laser import Laser
from sound import Sound
import os

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, offset: int, position=None) -> None:
        super().__init__()

        # Globais
        self.width = width
        self.height = height
        self.offset = offset
        self.speed = 6
        self.player_lives = 3

        # Carregar imagem da nave
        self.original_image = pygame.image.load('images/spaceship/spaceship.png')
        self.image = self.original_image.copy()
        
        if position:
            self.rect = self.image.get_rect(midbottom=position)
        else:
            self.rect = self.image.get_rect(midbottom=(self.width/2, self.height - 100))
        
        # Laser
        self.laser_ready = True
        self.laser_delay = 300
        self.laser_time = 0
        self.laser_group = pygame.sprite.Group()
        self.laser_sound = Sound().laser_sound

        # Super
        self.transformation_active = False
        self.transformation_time = 0

        # Sprites do Jogador
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(self)

    def get_user_input(self) -> None:
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
            self.rect.x += self.speed

        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]):
            self.rect.x -= self.speed

        elif (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.height)
            self.laser_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            try:
                self.laser_sound.play()
            except:
                pass  # Ignore se não conseguir tocar o som

    def constrains(self) -> None:
        if self.rect.right > (1415 - self.offset):
            self.rect.right = (1415 - self.offset)
        elif self.rect.left < (485 + self.offset):
            self.rect.left = (485 + self.offset)

    def recharge_laser(self) -> None:
        if not self.laser_ready:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
    
    def update(self) -> None:
        self.laser_group.update()
        self.get_user_input()
        self.constrains()
        self.recharge_laser()

    def super_spaceship(self) -> None:
        self.speed = 12
        # Transformar a nave (aumentar tamanho)
        self.image = pygame.transform.scale2x(self.original_image)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        self.laser_delay = 100
        self.transformation_time = pygame.time.get_ticks()

    def reset_transformation(self) -> None:
        self.speed = 6
        self.image = self.original_image.copy()
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
        self.laser_delay = 300
        self.transformation_active = False
        self.transformation_time = 0

    def reset(self) -> None:
        self.rect = self.image.get_rect(midbottom=(self.width/2, self.height - 100))
        self.laser_group.empty()
