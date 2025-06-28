import pygame, math
from spaceship import Spaceship

class BlackHole(pygame.sprite.Sprite):
    def __init__(self, spaceship: Spaceship, x: int, y: int, offset: int):
        super().__init__()
        
        self.__spaceship = spaceship
        self.__attraction_force = 5
        self.__speed = 2
        self.__direction = 1
        self.__offset = offset
        
        # Carregar e configurar a imagem do buraco negro
        self.__image = pygame.image.load('images/bg/black_hole.png')
        self.__rect = self.image.get_rect(center = (x, y))
        
        # Grupo de sprites
        self.__black_hole_group = pygame.sprite.Group()

    # Setters e Getters
    @property
    def spaceship(self):
        return self.__spaceship
    
    @spaceship.setter
    def spaceship(self, value):
        self.__spaceship = value
    
    @property
    def attraction_force(self):
        return self.__attraction_force
    
    @attraction_force.setter
    def attraction_force(self, value):
        self.__attraction_force = value

    @property
    def speed(self):
        return self.__speed
    
    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def direction(self):
        return self.__direction
    
    @direction.setter
    def direction(self, value):
        self.__direction = value

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
    def black_hole_group(self):
        return self.__black_hole_group
    
    @black_hole_group.setter
    def black_hole_group(self, value):
        self.__black_hole_group = value
    
    @property
    def offset(self):
        return self.__offset
    
    @offset.setter
    def offset(self, value):
        self.__offset = value

    # Métodos
    def move(self) -> None: # Movimentação
        # Move em direção ao jogador
        self.rect.x += self.direction * self.speed
        
        # Calcula a distância entre o buraco negro e a nave
        dx = self.spaceship.rect.centerx - self.rect.centerx
        dy = self.spaceship.rect.centery - self.rect.centery
        distance = math.sqrt(dx**2 + dy**2)
        
        # Aplica força gravitacional se estiver próximo
        if distance < 450:
            attraction = self.attraction_force * (1 - distance/450)
            self.spaceship.rect.x -= int((dx/distance) * attraction)
    
    def constrains_movement(self) -> None: # Restrições de Movimento
        if self.rect.right >= (1415 - self.offset):
            self.rect.right = (1415 - self.offset)
            self.direction = -1
        elif self.rect.left <= (485 + self.offset):
            self.rect.left = (485 + self.offset)
            self.direction = 1

    def create_black_hole(self) -> None: # Construtor
        self.black_hole_group.add(self)

    def destroy_black_hole(self) -> None: # Destrutor
        self.black_hole_group.empty()

    def update(self) -> None: # Atualiza
        if self.black_hole_group:
            self.move()
            self.constrains_movement()