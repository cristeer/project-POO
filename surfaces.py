import pygame
from fonts import Fonts

class Surfaces:
    
    def __init__(self, display, game):
        
        self.fonts = Fonts()
        self.display = display
        self.game = game

        self.life_icon = pygame.image.load('images/spaceship/spaceship.png')
        self.life_icon = pygame.transform.scale(self.life_icon, (40, 25))
        
        self.game_over_surface = self.fonts.font.render('GAME OVER', False, self.display.YELLOW)
        self.score_text_surface = self.fonts.font.render('SCORE', False, self.display.YELLOW)
        self.highscore_text_surface = self.fonts.font.render('HIGH-SCORE', False, self.display.YELLOW)
        self.level_surface = self.fonts.font.render(f'LEVEL {self.game.level:02}', False, self.display.YELLOW)

        self.main_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.main_bg = pygame.transform.smoothscale(self.main_bg, (self.display.screen_width, self.display.screen_height))

        self.game_bg = pygame.image.load('images/bg/background.png').convert_alpha()
        self.game_bg = pygame.transform.smoothscale(self.game_bg, (950, 1060))