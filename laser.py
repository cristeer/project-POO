import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position: tuple = None, speed: int = None, height: int = None):
        super().__init__()
        
        self.__YELLOW = (243, 216, 63)
        self.__speed = speed or 5
        self.__height = height or 800
        self.__image = pygame.Surface((8, 20))
        self.__rect = self.image.get_rect(center = position or (0, 0))
    
        self.image.fill(self.__YELLOW)
        
    # Setters e Getters
    @property
    def YELLOW(self):
        return self.__YELLOW

    @YELLOW.setter
    def YELLOW(self, value):
        self.__YELLOW = value

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

    # Métodos:
    def destroy(self) -> None:
        if self.rect.y + 20 > self.height or self.rect.y < 0:
            self.kill()
    
    def laser_move(self) -> None:
        self.rect.y -= self.speed

    def update(self) -> None:
        self.laser_move()
        self.destroy()
