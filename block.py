import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        
        self.__image = pygame.Surface((3, 3))
        self.__rect = self.image.get_rect(topleft=(x, y))

        self.image.fill((243, 216, 63))

    # Setters e Getters
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

