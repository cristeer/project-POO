import pygame
from fonts import Fonts

class Surfaces:
    
    def __init__(self, display, game):
        
        self.__fonts = Fonts()
        self.__display = display
        self.__game = game

        self.__life_icon = pygame.image.load('images/spaceship/spaceship.png')
        self.__life_icon = pygame.transform.scale(self.life_icon, (40, 25))
        
        self.__game_over_surface = self.fonts.font.render('GAME OVER', False, self.display.YELLOW)
        self.__score_text_surface = self.fonts.font.render('SCORE', False, self.display.YELLOW)
        self.__highscore_text_surface = self.fonts.font.render('HIGH-SCORE', False, self.display.YELLOW)
        self.__level_surface = self.fonts.font.render(f'LEVEL {self.game.level:02}', False, self.display.YELLOW)

        self.__main_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.__main_bg = pygame.transform.smoothscale(self.main_bg, (self.display.screen_width, self.display.screen_height))

        self.__game_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.__game_bg = pygame.transform.smoothscale(self.game_bg, (950, 1060))

        # self.__ranking_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        # self.__ranking_bg = pygame.transform.smoothscale(self.ranking_bg, (self.display.screen_width, self.display.screen_height))


    @property
    def fonts(self):
        return self.__fonts

    @fonts.setter
    def fonts(self, value):
        self.__fonts = value

    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, value):
        self.__display = value

    @property
    def game(self):
        return self.__game

    @game.setter
    def game(self, value):
        self.__game = value

    @property
    def life_icon(self):
        return self.__life_icon

    @life_icon.setter
    def life_icon(self, value):
        self.__life_icon = value

    @property
    def game_over_surface(self):
        return self.__game_over_surface

    @game_over_surface.setter
    def game_over_surface(self, value):
        self.__game_over_surface = value

    @property
    def score_text_surface(self):
        return self.__score_text_surface

    @score_text_surface.setter
    def score_text_surface(self, value):
        self.__score_text_surface = value

    @property
    def highscore_text_surface(self):
        return self.__highscore_text_surface

    @highscore_text_surface.setter
    def highscore_text_surface(self, value):
        self.__highscore_text_surface = value

    @property
    def level_surface(self):
        return self.__level_surface

    @level_surface.setter
    def level_surface(self, value):
        self.__level_surface = value

    @property
    def main_bg(self):
        return self.__main_bg

    @main_bg.setter
    def main_bg(self, value):
        self.__main_bg = value

    @property
    def game_bg(self):
        return self.__game_bg

    @game_bg.setter
    def game_bg(self, value):
        self.__game_bg = value

    # @property
    # def ranking_bg(self):
    #     return self.__ranking_bg

    # @ranking_bg.setter 
    # def ranking_bg(self, value):
    #     self.__ranking_bg = value