import pygame
from laser import Laser
class Spaceship(pygame.sprite.Sprite):
    def __init__(self, width: int, height: int, offset: int, sound = None, position = None) -> None:
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
        
        # Laser
        self.__current_time = 0
        self.__laser_ready = True
        self.__laser_delay = 300
        self.__laser_time = 0
        self.__laser_group = pygame.sprite.Group()
        self.__laser_sound = sound.laser_sound

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
    def get_user_input(self) -> None: #i Entrada do Usuário
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]): # Move Direita
            self.rect.x += self.speed

        elif (keys[pygame.K_LEFT] or keys[pygame.K_a]): # Move Esquerda
            self.rect.x -= self.speed

        elif (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.laser_ready: # Atira
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.height)
            self.laser_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()

    def movement_constrains(self) -> None: # Limitações de movimento
        if self.rect.right > (1415 - self.offset):
            self.rect.right = (1415 - self.offset)
        elif self.rect.left < (485 + self.offset):
            self.rect.left = (485 + self.offset)

    def recharge_laser(self) -> None: # Recarga dos lasers
        if not self.laser_ready:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
    
    def update(self) -> None: # Atualiza a nave
        self.laser_group.update()
        self.get_user_input()
        self.movement_constrains()
        self.recharge_laser()

    def super_spaceship(self) -> None: # Transformação Ativa
        self.speed = 12
        # Transformar a nave (aumentar tamanho)
        self.image = pygame.transform.scale2x(self.original_image)
        old_center = self.rect.center
        self.rect = self.image.get_rect(center = old_center)
        self.laser_delay = 100
        self.transformation_time = pygame.time.get_ticks()

    def reset_transformation(self) -> None: # Transformação Inativa
        self.speed = 6
        self.image = self.original_image.copy()
        old_center = self.rect.center
        self.rect = self.image.get_rect(center = old_center)
        self.laser_delay = 300
        self.transformation_active = False
        self.transformation_time = 0

    def reset_position(self) -> None: # Reinicia posição da Nave
        self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 100))
        self.laser_group.empty()

    def destroy_spaceship(self): # Destrutor
        self.reset_position()
        self.transformation_active = False 
        self.transformation_time = 0
        self.spaceship_group.empty()
        self.spaceship_group.add(self)

    def __sub__(self, value):
        if isinstance(value, int):
            self.player_lives -= value
            if self.player_lives < 0:
                self.player_lives = 0
            return self 

    def __eq__(self, value):
        if isinstance(value, int):
            return self.player_lives == value
        
    def __hash__(self):
        return id(self)
    
    # Necessário pois o hash, ao executar uma das sobrecargas acima, vem por padrão como None, mas pygame.sprite.Sprite requer que todos os membros possuam hash, logo, esta linha é necessária para sanar o problema