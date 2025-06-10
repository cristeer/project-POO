import pygame, sys
from button import Button

class Display:
    def __init__(self, game):
        self.GREY = (29, 29, 27)
        self.YELLOW = (243, 216, 63)

        self.screen_width = game.screen_width
        self.screen_height = game.screen_height
        self.offset = game.offset
        
        # Setup
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Space Invaders')
        
        # Tentar carregar fonte personalizada
        try:
            self.font = pygame.font.Font('fonts/monogram.ttf', 50)
        except:
            self.font = pygame.font.Font(None, 50)
            
        self.game = game

        # Carregar ícone de vida
        try:
            self.life_icon = pygame.image.load('images/spaceship/spaceship.png')
            self.life_icon = pygame.transform.scale(self.life_icon, (40, 25))
        except:
            # Fallback se não encontrar a imagem
            self.life_icon = pygame.Surface((40, 25))
            self.life_icon.fill((0, 255, 0))
        
        self.game_over_surface = self.font.render('GAME OVER', False, self.YELLOW)
        self.score_text_surface = self.font.render('SCORE', False, self.YELLOW)
    
    def game_elements(self) -> None: # Desenhar sprites
        self.game.spaceship.spaceship_group.draw(self.screen)
        self.game.spaceship.laser_group.draw(self.screen)
        self.game.alien.aliens_group.draw(self.screen)
        self.game.alien.aliens_lasers_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_lasers_group.draw(self.screen)
        for obstacle in self.game.obstacles:
            obstacle.blocks_group.draw(self.screen)

    def ui_elements(self) -> None: # Desenhar bordas do jogo
        pygame.draw.rect(self.screen, self.YELLOW, (485, 10, 950, 1060), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(self.screen, self.YELLOW, (505, 1010), (1415, 1010), 3)
        level_surface = self.font.render(f'LEVEL {self.game.level:02}', False, self.YELLOW)
        self.screen.blit(level_surface, (1225, 1020))
        
        x = 520
        for life in range(self.game.spaceship.player_lives):
            self.screen.blit(self.life_icon, (x, 1020))
            x += 45
            
        self.screen.blit(self.score_text_surface, (520, 25))
        formatted_score = str(self.game.score).zfill(6)
        score_surface = self.font.render(formatted_score, False, self.YELLOW)
        self.screen.blit(score_surface, (520, 50))

    def draw_game(self):
        self.screen.fill(self.GREY)

        if self.game.game_state:
            self.ui_elements()
            self.game_elements()

        else:
            self.main_menu()
            pygame.display.flip()
        

    def main_menu(self):
        # Sobrepõe a imagem
        self.screen.fill(self.GREY)

        # Título
        self.title_font = pygame.font.Font('fonts/monogram.ttf', 100)
        self.button_font = pygame.font.Font('fonts/monogram.ttf', 80)
        self.GAME_TITLE = self.title_font.render("SPACE INVADERS", True, self.YELLOW)
        self.GAME_TITLE_RECT = self.GAME_TITLE.get_rect(center = (960, 200))
         
        # Botões
        self.play_button = Button(image = None, pos = (960, 490), text_input = 'Play', font = self.button_font,base_color = "White", hovering_color = "#b68f40")
        
        self.settings_button = Button(image = None, pos = (960, 640), text_input = 'Settings', font = self.button_font,base_color = "White", hovering_color = "#b68f40")
        
        self.ranking_button = Button(image = None, pos = (960, 790), text_input = 'Ranking', font = self.button_font,base_color = "White", hovering_color = "#b68f40")

        self.quit_button = Button(image = None, pos = (960, 940), text_input = 'Quit', font = self.button_font,base_color = "White", hovering_color = "#b68f40")

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
                    pass

                if self.ranking_button.checkForInput(MOUSE_POS):
                    pass