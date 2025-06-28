import pygame
from fonts import Fonts

class Surfaces:   
    def __init__(self, display, game):        
        self.__fonts = Fonts()
        self.__display = display
        self.__game = game

        # Icones de vida do Jogador
        self.__life_icon = pygame.image.load('images/spaceship/spaceship.png')
        self.__life_icon = pygame.transform.scale(self.life_icon, (40, 25))
        
        # Textos Básicos
        self.__game_over_surface = self.fonts.font.render('GAME OVER', False, self.display.YELLOW)
        self.__score_text_surface = self.fonts.font.render('SCORE', False, self.display.YELLOW)
        self.__highscore_text_surface = self.fonts.font.render('HIGH-SCORE', False, self.display.YELLOW)
        self.__level_surface = self.fonts.font.render(f'LEVEL {self.game.level:02}', False, self.display.YELLOW)
        
        # Título do Jogo
        self.__GAME_TITLE = self.fonts.title_font.render("SPACE INVADERS", True, self.display.YELLOW)
        self.__GAME_TITLE_RECT = self.GAME_TITLE.get_rect(center = (960, 200))

        # Título do Menu de Ranking
        self.__ranking_title = self.fonts.title_font.render("RANKING", True, self.display.YELLOW)
        self.__ranking_title_rect = self.ranking_title.get_rect(center = (960, 200))

        # Fundo do Menu
        self.__main_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.__main_bg = pygame.transform.smoothscale(self.main_bg, (self.display.screen_width, self.display.screen_height))

        # Fundo do Jogo
        self.__game_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.__game_bg = pygame.transform.smoothscale(self.game_bg, (950, 1060))

        # Entrada de Nome
        self.__enter_name = self.fonts.button_font.render("Enter Your Name", True, self.display.YELLOW)
        self.__enter_name_rect = self.enter_name.get_rect(center = (960, 300))

        # Settings
        self.__settings_title = self.fonts.title_font.render("SETTINGS", True, self.display.YELLOW)
        self.__settings_title_rect = self.settings_title.get_rect(center = (960, 200))

    # Getters e Setters
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

    @property
    def GAME_TITLE(self):
        return self.__GAME_TITLE

    @GAME_TITLE.setter
    def GAME_TITLE(self, value):
        self.__GAME_TITLE = value

    @property
    def GAME_TITLE_RECT(self):
        return self.__GAME_TITLE_RECT

    @GAME_TITLE_RECT.setter
    def GAME_TITLE_RECT(self, value):
        self.__GAME_TITLE_RECT = value

    @property
    def ranking_title(self):
        return self.__ranking_title

    @ranking_title.setter
    def ranking_title(self, value):
        self.__ranking_title = value

    @property
    def ranking_title_rect(self):
        return self.__ranking_title_rect

    @ranking_title_rect.setter
    def ranking_title_rect(self, value):
        self.__ranking_title_rect = value

    @property
    def enter_name(self):
        return self.__enter_name

    @enter_name.setter
    def enter_name(self, value):
        self.__enter_name = value

    @property
    def enter_name_rect(self):
        return self.__enter_name_rect

    @enter_name_rect.setter
    def enter_name_rect(self, value):
        self.__enter_name_rect = value

    @property
    def settings_title(self):
        return self.__settings_title

    @settings_title.setter
    def settings_title(self, value):
        self.__settings_title = value

    @property
    def settings_title_rect(self):
        return self.__settings_title_rect

    @settings_title_rect.setter
    def settings_title_rect(self, value):
        self.__settings_title_rect = value
        
    # Métodos
    def draw_entry_box(self, name:str) -> None: # Campo de entrada
        input_box = pygame.Rect(710, 400, 500, 70)
        txt_surface = self.fonts.button_font.render(name, True, self.display.YELLOW)
        self.game.screen.blit(txt_surface, (input_box.x + 20, input_box.y - 5))
        pygame.draw.rect(self.game.screen, self.display.YELLOW, input_box, 2)
