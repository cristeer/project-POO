import pygame
import os

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
    
    def draw_hud(self):
        self.screen.fill(self.GREY)

        # Exibe o menu de vidas se houver jogo rodando
        if self.game.game_state:
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
        else:
            self.screen.blit(self.game_over_surface, (self.screen_width//2 - 150, self.screen_height//2))
            start_text = self.font.render('Press SPACE to start', False, self.YELLOW)
            self.screen.blit(start_text, (self.screen_width//2 - 200, self.screen_height//2 + 50))
        
        # Desenhar bordas do jogo
        pygame.draw.rect(self.screen, self.YELLOW, (485, 10, 950, 1060), 2, 0, 60, 60, 60, 60)
        pygame.draw.line(self.screen, self.YELLOW, (505, 1010), (1415, 1010), 3)
        
        # Desenhar sprites
        self.game.spaceship.spaceship_group.draw(self.screen)
        self.game.spaceship.laser_group.draw(self.screen)
        self.game.alien.aliens_group.draw(self.screen)
        self.game.alien.aliens_lasers_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_group.draw(self.screen)
        self.game.mystery_ship.mystery_ship_lasers_group.draw(self.screen)

        for obstacle in self.game.obstacles:
            obstacle.blocks_group.draw(self.screen)