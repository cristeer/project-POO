import pygame, sys, os

from button import Button
from fonts import Fonts
from surfaces import Surfaces
from settings import Settings

class Display:
    def __init__(self, game):
        self.__game = game
        
        # Cores
        self.__GREY = (29, 29, 27)
        self.__YELLOW = (243, 216, 63)
        
        # Variáveis Ercã
        self.__screen_width = game.screen_width
        self.__screen_height = game.screen_height
        self.__offset = game.offset
        self.__screen = game.screen

        # Instância de outras classes
        self.__fonts = Fonts()
        self.__surfaces = Surfaces(self, game)
        self.__settings = Settings(self)

        # Scroll control
        self.__bg_scroll_y = 0
        self.__bg_scroll_speed = 1
         
        # Botões
        self.__play_button = Button(
                pos = (960, 490),
                text_input = '',
                text_font = self.fonts.button_font,
                base_color = "White",
                hovering_color = "#b68f40"
            )

        self.__settings_button = Button(
            pos = (960, 640),
            text_input = 'Ajustes',
            text_font = self.fonts.button_font,
            base_color = "White", 
            hovering_color = "#b68f40"
        )
    
        self.__ranking_button = Button(
            pos = (960, 790),
            text_input = 'Ranking', 
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.__quit_button = Button(
            pos = (960, 940),
            text_input = 'Sair',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.__continue_button = Button(
            pos=(960, 490),
            text_input='Continue',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        self.__back_button_pause = Button(
            pos=(960, 640),
            text_input='Voltar',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        self.__back_button_ranking = Button(
            pos=(960, 1000),
            text_input='Voltar',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )

    #Settters e Getters
    @property
    def game(self):
        return self.__game

    @game.setter
    def game(self, value):
        self.__game = value

    @property
    def GREY(self):
        return self.__GREY

    @GREY.setter
    def GREY(self, value):
        self.__GREY = value

    @property
    def YELLOW(self):
        return self.__YELLOW

    @YELLOW.setter
    def YELLOW(self, value):
        self.__YELLOW = value

    @property
    def screen_width(self):
        return self.__screen_width

    @screen_width.setter
    def screen_width(self, value):
        self.__screen_width = value

    @property
    def screen_height(self):
        return self.__screen_height

    @screen_height.setter
    def screen_height(self, value):
        self.__screen_height = value

    @property
    def offset(self):
        return self.__offset

    @offset.setter
    def offset(self, value):
        self.__offset = value

    @property
    def screen(self):
        return self.__screen

    @screen.setter
    def screen(self, value):
        self.__screen = value

    @property
    def fonts(self):
        return self.__fonts

    @fonts.setter
    def fonts(self, value):
        self.__fonts = value

    @property
    def surfaces(self):
        return self.__surfaces

    @surfaces.setter
    def surfaces(self, value):
        self.__surfaces = value

    @property
    def settings(self):
        return self.__settings

    @settings.setter
    def settings(self, value):
        self.__settings = value

    @property
    def bg_scroll_y(self):
        return self.__bg_scroll_y

    @bg_scroll_y.setter
    def bg_scroll_y(self, value):
        self.__bg_scroll_y = value

    @property
    def bg_scroll_speed(self):
        return self.__bg_scroll_speed

    @bg_scroll_speed.setter
    def bg_scroll_speed(self, value):
        self.__bg_scroll_speed = value

    @property
    def play_button(self):
        return self.__play_button

    @play_button.setter
    def play_button(self, value):
        self.__play_button = value

    @property
    def settings_button(self):
        return self.__settings_button

    @settings_button.setter
    def settings_button(self, value):
        self.__settings_button = value

    @property
    def ranking_button(self):
        return self.__ranking_button

    @ranking_button.setter
    def ranking_button(self, value):
        self.__ranking_button = value

    @property
    def quit_button(self):
        return self.__quit_button

    @quit_button.setter
    def quit_button(self, value):
        self.__quit_button = value

    @property
    def continue_button(self):
        return self.__continue_button

    @continue_button.setter
    def continue_button(self, value):
        self.__continue_button = value

    @property
    def back_button_pause(self):
        return self.__back_button_pause

    @back_button_pause.setter
    def back_button_pause(self, value):
        self.__back_button_pause = value

    @property
    def back_button_ranking(self):
        return self.__back_button_ranking

    @back_button_ranking.setter
    def back_button_ranking(self, value):
        self.__back_button_ranking = value

    # Métodos
    def update_menu_buttons(self) -> None:
        if os.path.exists('save_game.json'):
            self.play_button = Button(
                pos = (960, 490),
                text_input = 'Continue',
                text_font = self.fonts.button_font,
                base_color = "White",
                hovering_color = "#b68f40"
            )
        else:
            self.play_button = Button(
                pos = (960, 490),
                text_input = 'Jogar',
                text_font = self.fonts.button_font,
                base_color = "White",
                hovering_color = "#b68f40"
            )

    def update_background_position(self) -> None: # Atualiza a posição de fundo
        self.bg_scroll_y = (self.bg_scroll_y + self.bg_scroll_speed) % 1060

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

    def ui_elements(self) -> None: # Desenhar bordas do jogo
        # Exibe as linhas
        pygame.draw.rect(self.screen, self.YELLOW, (485, 10, 950, 1060), 2, 0)
        pygame.draw.line(self.screen, self.YELLOW, (505, 1010), (1415, 1010), 3)

        # Formata score
        formatted_score = str(self.game.score).zfill(6)
        score_surface = self.fonts.font.render(formatted_score, False, self.YELLOW)
        self.screen.blit(score_surface, (520, 50))

        self.screen.blit(self.surfaces.highscore_text_surface, (1225, 25))
        formatted_highscore = str(self.game.highscore).zfill(6)
        highscore_surface = self.fonts.font.render(formatted_highscore, False, self.YELLOW)
        self.screen.blit(highscore_surface, (1225, 50))

        # Exibe nível
        self.screen.blit(self.surfaces.level_surface, (1225, 1020))

        # Exibe vida do jogador
        x = 520
        for life in range(self.game.spaceship.player_lives):
            self.screen.blit(self.surfaces.life_icon, (x, 1020))
            x += 45
            
        self.screen.blit(self.surfaces.score_text_surface, (520, 25))

    def draw_game(self) -> None: # Exibe todos elementos visuais do jogo
        self.screen.fill(self.GREY)
        self.update_menu_buttons()
        
        if self.settings.settings_state:
            self.settings.draw_settings(self.game.events)
            return
        
        if self.game.game_state:            
            # Rolagem Vertical
            self.update_background_position()
            self.screen.blit(self.surfaces.game_bg, (485, 10 + self.bg_scroll_y))
            self.screen.blit(self.surfaces.game_bg, (485, 10 + self.bg_scroll_y - 1060))
            
            self.ui_elements()
            self.game_elements()
        else:
            self.main_menu(self.game.events)
        
        pygame.display.flip()

    def main_menu(self, events) -> None: # Recebe eventos como argumento
        self.screen.blit(self.surfaces.main_bg, (0,0))

        MOUSE_POS = pygame.mouse.get_pos()

        # Exibe o menu
        self.screen.blit(self.surfaces.GAME_TITLE, self.surfaces.GAME_TITLE_RECT)
        
        for button in [self.play_button, self.settings_button, self.ranking_button, self.quit_button]:
            button.change_color(MOUSE_POS)
            button.update(self.screen)
        
        for event in events:  # Use os eventos recebidos
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.check_for_input(MOUSE_POS):
                    if os.path.exists('save_game.json'):
                        self.game.save.load_game()
                    else:
                        self.game.reset_game()
                    return

                if self.quit_button.check_for_input(MOUSE_POS):
                    pygame.quit()
                    sys.exit()

                if self.settings_button.check_for_input(MOUSE_POS):
                    self.settings.settings_state = True
                    return

                if self.ranking_button.check_for_input(MOUSE_POS):
                    self.draw_ranking()


    def pause_menu(self, events) -> None: # Menu de pausa, ao pressionar ESC durante o jogo
        # Desenha Semi transparência
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        self.screen.blit(overlay, (0, 0))

        while True:
            events = pygame.event.get()
            
            MOUSE_POS = pygame.mouse.get_pos()
            for button in [self.continue_button, self.back_button_pause]:
                button.change_color(MOUSE_POS)
                button.update(self.screen)

            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return 'pause'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.continue_button.check_for_input(MOUSE_POS):
                        return 'pause'
                    if self.back_button_pause.check_for_input(MOUSE_POS):
                        self.game.save.save_game()
                        return 'menu'

            pygame.display.flip()
            self.game.clock.tick(60)

    def draw_ranking(self) -> None: # Desenha o ranking 
        while True:
            self.screen.blit(self.surfaces.main_bg, (0, 0))

            self.screen.blit(self.surfaces.ranking_title, self.surfaces.ranking_title_rect)

            self. __list_players()

            MOUSE_POS = pygame.mouse.get_pos()
            self.back_button_ranking.change_color(MOUSE_POS)
            self.back_button_ranking.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_button_ranking.check_for_input(MOUSE_POS):
                        return
                    
            pygame.display.flip()
            self.game.clock.tick(60)
      
    def __list_players(self) -> None: # Lista os jogadores
        scores = self.game.ranking.get_ranking()
        y_pos = 350

        for i, score_entry in enumerate(scores, 1):
            score_text = self.fonts.button_font.render (f"#{i} {score_entry['name']}: {score_entry['score']:06d}", True, self.YELLOW)
            score_rect = score_text.get_rect(center = (960, y_pos))
            self.screen.blit(score_text, score_rect)
            y_pos += 60 

    def get_player_name(self) -> None: # Jogador entra com nome ao fim da partida.
        name = ''
        input_active = True

        while input_active:
            self.screen.blit(self.surfaces.main_bg, (0,0))
            self.screen.blit(self.surfaces.enter_name, self.surfaces.enter_name_rect)
            self.surfaces.draw_entry_box(name)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and name.strip():
                        return name
                    
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]

                    else:
                        if len(name) < 10 and event.unicode.isalnum():
                            name += event.unicode

            pygame.display.flip()
            self.game.clock.tick(60)