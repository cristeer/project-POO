import pygame

class Fonts:

    def __init__(self):
        
        self.__font = pygame.font.Font('fonts/monogram.ttf', 50)
        self.__title_font = pygame.font.Font('fonts/monogram.ttf', 100)
        self.__button_font = pygame.font.Font('fonts/monogram.ttf', 80)

    # Setters e Getters
    @property
    def font(self):
        return self.__font

    @font.setter
    def font(self, value):
        self.__font = value

    @property
    def title_font(self):
        return self.__title_font

    @title_font.setter
    def title_font(self, value):
        self.__title_font = value

    @property
    def button_font(self):
        return self.__button_font

    @button_font.setter
    def button_font(self, value):
        self.__button_font = value
