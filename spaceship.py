import pygame
from laser import Laser
from sound import Sound

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, offset: int, position=None) -> None:
        super().__init__()

        # Globais
        self.__width = width
        self.__height = height
        self.__offset = offset
        self.__speed = 6
        self.__player_lives = 3

        # Carregar imagem da nave
        self.__original_image = pygame.image.load('images/spaceship/spaceship.png')
        self.__image = self.original_image.copy()
        
        if position:
            self.rect = self.image.get_rect(midbottom = position) #Definido como publico devido a ser um requisito do pygame para funcionamento dos sprites
        else:
            self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 100))
        
        self.__current_time = 0 #Possivel problema de encapsulamento

        # Laser
        self.__laser_ready = True
        self.__laser_delay = 300
        self.__laser_time = 0
        self.__laser_group = pygame.sprite.Group()
        self.__laser_sound = Sound().laser_sound

        # Super
        self.__transformation_active = False
        self.__transformation_time = 0

        # Sprites do Jogador
        self.__spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(self)

    # Setters e Getters
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def player_lives(self):
        return self.__player_lives

    @player_lives.setter
    def player_lives(self, value):
        self.__player_lives = value

    @property
    def original_image(self):
        return self.__original_image

    @original_image.setter
    def original_image(self, value):
        self.__original_image = value

    @property
    def image(self):
        return self.__image

    @image.setter
    def image(self, value):
        self.__image = value
    
    @property
    def current_time(self):
        return self.__current_time
    
    @current_time.setter
    def current_time(self, value):
        self.__current_time = value

    @property
    def laser_ready(self):
        return self.__laser_ready

    @laser_ready.setter
    def laser_ready(self, value):
        self.__laser_ready = value

    @property
    def laser_delay(self):
        return self.__laser_delay

    @laser_delay.setter
    def laser_delay(self, value):
        self.__laser_delay = value

    @property
    def laser_time(self):
        return self.__laser_time

    @laser_time.setter
    def laser_time(self, value):
        self.__laser_time = value

    @property
    def laser_group(self):
        return self.__laser_group

    @laser_group.setter
    def laser_group(self, value):
        self.__laser_group = value

    @property
    def laser_sound(self):
        return self.__laser_sound

    @laser_sound.setter
    def laser_sound(self, value):
        self.__laser_sound = value
    
    @property
    def transformation_active(self):
        return self.__transformation_active

    @transformation_active.setter
    def transformation_active(self, value):
        self.__transformation_active = value

    @property
    def transformation_time(self):
        return self.__transformation_time

    @transformation_time.setter
    def transformation_time(self, value):
        self.__transformation_time = value

    @property
    def spaceship_group(self):
        return self.__spaceship_group
    
    @spaceship_group.setter
    def spaceship_group(self, value):
        self.__spaceship_group = value

    # Métodos
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
        self.rect = self.image.get_rect(center = old_center)
        self.laser_delay = 100
        self.transformation_time = pygame.time.get_ticks()

    def reset_transformation(self) -> None:
        self.speed = 6
        self.image = self.original_image.copy()
        old_center = self.rect.center
        self.rect = self.image.get_rect(center = old_center)
        self.laser_delay = 300
        self.transformation_active = False
        self.transformation_time = 0

    def reset(self) -> None:
        self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 100))
        self.laser_group.empty()
