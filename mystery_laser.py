import pygame
from laser import Laser

class MysteryLaser(Laser):
    def __init__(self, position: tuple, speed: int, height: int, spaceship_group):
    
        self.__RED = (255, 0, 0)
        self.__speed = speed
        self.__height = height
        self.__spaceship_group = spaceship_group
        self.__image = pygame.Surface((32, 80))
        
        super().__init__(position, speed, height)
        
        self.__rect = self.image.get_rect(center = position)
        
        # Preeche o laser
        self.image.fill(self.RED)

    # Setters e Getters
    @property
    def RED(self):
        return self.__RED

    @RED.setter
    def RED(self, value):
        self.__RED = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def spaceship_group(self):
        return self.__spaceship_group

    @spaceship_group.setter
    def spaceship_group(self, value):
        self.__spaceship_group = value

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

    # Métodos
    def destroy_mystery_laser(self):
        if self.rect.y + 60 > self.height or self.rect.y < 0:
            self.kill()
    
    def mystery_laser_move(self):
        self.rect.y -= self.speed
        if self.spaceship_group.sprite:
            self.rect.x = self.spaceship_group.sprite.rect.x

    def update(self):
        self.mystery_laser_move()
        self.destroy_mystery_laser()
