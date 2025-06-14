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

    def draw_score(self):
        # Score
        formatted_score = str(self.game.score).zfill(6)
        score_surface = self.fonts.font.render(formatted_score, False, self.display.YELLOW)
        self.display.screen.blit(self.score_text_surface, (520, 25))
        self.display.screen.blit(score_surface, (520, 50))

        # Highscore
        self.display.screen.blit(self.highscore_text_surface, (1225, 25))
        formatted_highscore = str(self.game.highscore).zfill(6)
        highscore_surface = self.fonts.font.render(formatted_highscore, False, self.display.YELLOW)
        self.display.screen.blit(highscore_surface, (1225, 50))

    def draw_hud(self):
        # Exibe o Hud
        pygame.draw.rect(self.display.screen, self.display.YELLOW, (485, 10, 950, 1060), 2, 0)
        pygame.draw.line(self.display.screen, self.display.YELLOW, (505, 1010), (1415, 1010), 3)
        self.display.screen.blit(self.level_surface, (1225, 1020))

        # exibe as vidas
        x = 520
        for life in range(self.game.spaceship.player_lives):
            self.display.screen.blit(self.life_icon, (x, 1020))
            x += 45

    def update_background_position(self):
        self.display.bg_scroll_y = (self.display.bg_scroll_y + self.display.bg_scroll_speed) % 1060

    def draw_bg(self):
            self.display.screen.blit(self.game_bg, (485, 10 + self.display.bg_scroll_y))
            self.display.screen.blit(self.game_bg, (485, 10 + self.display.bg_scroll_y - 1060))
            self.update_background_position()