import pygame, sys, os

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
         
        # Botões
        self.play_button = Button(
                pos = (960, 490),
                text_input = '',
                text_font = self.fonts.button_font,
                base_color = "White",
                hovering_color = "#b68f40"
            )

        self.settings_button = Button(
            pos = (960, 640),
            text_input = 'Settings',
            text_font = self.fonts.button_font,
            base_color = "White", 
            hovering_color = "#b68f40"
        )
    
        self.ranking_button = Button(
            pos = (960, 790),
            text_input = 'Ranking', 
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.quit_button = Button(
            pos = (960, 940),
            text_input = 'Quit',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.continue_button = Button(
            pos=(960, 490),
            text_input='Continue',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        self.back_button_pause = Button(
            pos=(960, 640),
            text_input='Back to Menu',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        self.back_button_ranking = Button(
            pos=(960, 1000),
            text_input='Back to Menu',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )

    def update_menu_buttons(self):
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
                text_input = 'Play',
                text_font = self.fonts.button_font,
                base_color = "White",
                hovering_color = "#b68f40"
            )

    def update_background_position(self):
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

        pygame.draw.rect(self.screen, self.YELLOW, (485, 10, 950, 1060), 2, 0)
        pygame.draw.line(self.screen, self.YELLOW, (505, 1010), (1415, 1010), 3)

        # Fix score rendering
        formatted_score = str(self.game.score).zfill(6)
        score_surface = self.fonts.font.render(formatted_score, False, self.YELLOW)
        self.screen.blit(score_surface, (520, 50))

        self.screen.blit(self.surfaces.highscore_text_surface, (1225, 25))
        formatted_highscore = str(self.game.highscore).zfill(6)
        highscore_surface = self.fonts.font.render(formatted_highscore, False, self.YELLOW)
        self.screen.blit(highscore_surface, (1225, 50))

        # Fix level display
        self.screen.blit(self.surfaces.level_surface, (1225, 1020))

        # Fix life icon
        x = 520
        for life in range(self.game.spaceship.player_lives):
            self.screen.blit(self.surfaces.life_icon, (x, 1020))
            x += 45
            
        self.screen.blit(self.surfaces.score_text_surface, (520, 25))


    def draw_game(self):
        
        self.screen.fill(self.GREY)
        self.update_menu_buttons()
        
        if self.settings.settings_state:
            self.settings.draw_settings()
            return
        
        if self.game.game_state:
            self.update_background_position()
            
            # Scroll Vertical
            self.screen.blit(self.surfaces.game_bg, (485, 10 + self.bg_scroll_y))
            self.screen.blit(self.surfaces.game_bg, (485, 10 + self.bg_scroll_y - 1060))
            
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

        MOUSE_POS = pygame.mouse.get_pos()

        # Exibe o menu
        self.screen.blit(self.GAME_TITLE, self.GAME_TITLE_RECT)
        
        for button in [self.play_button, self.settings_button, self.ranking_button, self.quit_button]:
            button.change_color(MOUSE_POS)
            button.update(self.screen)
        
        for event in pygame.event.get():
            
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

    def pause_menu(self, events):
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


    def draw_ranking(self):
        while True:
            self.screen.fill(self.GREY)

            ranking_title = self.fonts.title_font.render("______RANKING______", True, self.YELLOW)
            ranking_title_rect = ranking_title.get_rect(center = (960, 200))
            self.screen.blit(ranking_title, ranking_title_rect)

            scores = self.game.ranking.get_ranking()
            y_pos = 350

            for i, score_entry in enumerate(scores, 1):
                score_text = self.fonts.button_font.render (f"#{i} {score_entry['name']}: {score_entry['score']:06d}", True, self.YELLOW)

                score_rect = score_text.get_rect(center = (960, y_pos))

                self.screen.blit(score_text, score_rect)
                y_pos += 60

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
    def get_player_name(self):
        name = ''
        input_active = True

        while input_active:
            self.screen.blit(self.surfaces.main_bg, (0,0))

            # Título
            title = self.fonts.title_font.render("Enter Your Name", True, self.YELLOW)
            title_rect = title.get_rect(center = (960, 300))
            self.screen.blit(title, title_rect)

            # Campo de entrada
            input_box = pygame.Rect(710, 400, 500, 60)
            txt_surface = self.fonts.button_font.render(name, True, self.YELLOW)
            self.screen.blit(txt_surface, (input_box.x + 20, input_box.y - 5))
            pygame.draw.rect(self.screen, self.YELLOW, input_box, 2)

            pygame.display.flip()
            #self.game.clock.tick(60)

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

