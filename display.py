import pygame, sys

from button import Button
from fonts import Fonts
from surfaces import Surfaces
from settings import Settings

class Display:
    def __init__(self, game):

        self.game = game

        self.GREY = (29, 29, 27)
        self.YELLOW = (243, 216, 63)

        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.offset = game.offset
        self.screen = game.screen

        self.fonts = Fonts()
        self.surfaces = Surfaces(self, game)
        self.settings = Settings(self)

        # Scroll control
        self.bg_scroll_y = 0
        self.bg_scroll_speed = 1

    def game_elements(self) -> None: # Desenhar sprites

        self.game.spaceship.spaceship_group.draw(self.screen)
        self.game.spaceship.laser_group.draw(self.screen)
        self.game.alien.aliens_group.draw(self.screen)
        self.game.alien.aliens_lasers_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_lasers_group.draw(self.screen)
        self.game.black_hole.black_hole_group.draw(self.screen)

        for obstacle in self.game.obstacles:
            obstacle.blocks_group.draw(self.screen)


    def ui_elements(self) -> None: # Faz o HUD
        self.surfaces.draw_score()
        self.surfaces.draw_hud()
        

    def draw_game(self) -> None: # Exibe os elemntos do jogo
        self.screen.fill(self.GREY)

        if self.settings.settings_state:
            self.settings.draw_settings()
            return
        
        if self.game.game_state:
            # Fundo e sua Lógica de Scroll
            self.surfaces.draw_bg()
            self.ui_elements()
            self.game_elements()
        else:
            self.main_menu()
            
        pygame.display.flip()

    def main_menu(self):

        self.screen.blit(self.surfaces.main_bg, (0,0))

        # Título
        self.GAME_TITLE = self.fonts.title_font.render("SPACE INVADERS", True, self.YELLOW)
        self.GAME_TITLE_RECT = self.GAME_TITLE.get_rect(center = (960, 200))
         
        # Botões
        self.play_button = Button(pos = (960, 490), text_input = 'Play', text_font = self.fonts.button_font,base_color = "White", hovering_color = "#b68f40")
        
        self.settings_button = Button(pos = (960, 640), text_input = 'Settings', text_font = self.fonts.button_font,base_color = "White", hovering_color = "#b68f40")
        
        self.ranking_button = Button(pos = (960, 790), text_input = 'Ranking', text_font = self.fonts.button_font,base_color = "White", hovering_color = "#b68f40")

        self.quit_button = Button(pos = (960, 940), text_input = 'Quit', text_font = self.fonts.button_font,base_color = "White", hovering_color = "#b68f40")

        MOUSE_POS = pygame.mouse.get_pos()

        # Exibe o menu
        self.screen.blit(self.GAME_TITLE, self.GAME_TITLE_RECT)
        
        for button in [self.play_button, self.settings_button, self.ranking_button, self.quit_button]:
            button.changeColor(MOUSE_POS)
            button.update(self.screen)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.checkForInput(MOUSE_POS):
                    self.game.reset_game()
                    return

                if self.quit_button.checkForInput(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                if self.settings_button.checkForInput(MOUSE_POS):
                    self.settings.settings_state = True
                    return

                if self.ranking_button.checkForInput(MOUSE_POS):
                    pass