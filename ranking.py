import json, pygame, sys
class Ranking:
    def __init__(self, game):
        self.game = game
        self.scores = {}
        self.MAX = 10
        self.ranking_state = False
        self.load_ranking()

    def add_score(self, player_name: str, score: int) -> None:
        # Add new score
        self.scores[player_name] = score
        
        # Sort scores and keep only top MAX scores
        sorted_scores = dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True)[:self.MAX])
        
        # Update scores dictionary
        self.scores = sorted_scores
        
        # Save to file
        self.save_ranking()

    def load_ranking(self) -> None:
        try:
            with open('ranking_file.json', 'r') as file:
                self.scores = json.load(file)
        except FileNotFoundError:
            self.scores = {}

    def save_ranking(self) -> None:
        with open('ranking_file.json', 'w') as file:
            json.dump(self.scores, file)

    def get_ranking(self) -> dict:
        return self.scores

    def get_player_name(self) -> str:
        input_text = ""
        input_active = True

        while input_active:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and input_text.strip():
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    elif len(input_text) < 10:  # Limit name length
                        if event.unicode.isalnum() or event.unicode.isspace():
                            input_text += event.unicode

            # Draw input screen
            self.game.screen.fill((0, 0, 0))

            # Draw title
            game_over_text = self.game.display.fonts.title_font.render('GAME OVER', False, self.game.display.YELLOW)
            game_over_rect = game_over_text.get_rect(center = (self.game.screen_width // 2, self.game.screen_height // 3))

            # Draw score
            score_text = self.game.display.fonts.font.render(f'Score: {self.game.score}', False, self.game.display.YELLOW)
            score_rect = score_text.get_rect(center = (self.game.screen_width // 2, game_over_rect.bottom + 50))

            # Draw input prompt
            prompt_text = self.game.display.fonts.font.render('Enter your name:', False, self.game.display.YELLOW)
            prompt_rect = prompt_text.get_rect(center = (self.game.screen_width // 2, score_rect.bottom + 50))

            # Draw input text
            input_surface = self.game.display.fonts.font.render(input_text + '|', False, self.game.display.YELLOW)
            input_rect = input_surface.get_rect(center=(self.game.screen_width // 2, prompt_rect.bottom + 30))

            # Draw everything
            self.game.screen.blit(game_over_text, game_over_rect)
            self.game.screen.blit(score_text, score_rect)
            self.game.screen.blit(prompt_text, prompt_rect)
            self.game.screen.blit(input_surface, input_rect)

            pygame.display.flip()
            self.game.clock.tick(60)

    def draw_ranking(self) -> None:
        while self.ranking_state:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.ranking_state = False
                        return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if return_button_rect.collidepoint(mouse_pos):
                        self.ranking_state = False
                        return

            # Clear screen
            self.game.screen.fill((0, 0, 0))
            
            # Draw title
            title = self.game.display.fonts.title_font.render('RANKING', False, self.game.display.YELLOW)
            title_rect = title.get_rect(center=(self.game.screen_width // 2, 100))
            self.game.screen.blit(title, title_rect)
            
            # Sort scores by value (descending)
            sorted_scores = dict(sorted(self.scores.items(), key=lambda x: x[1], reverse=True)[:self.MAX])
            
            # Draw scores
            y_position = 250
            for i, (name, score) in enumerate(sorted_scores.items(), 1):
                score_text = self.game.display.fonts.font.render(f'{i}. {name}: {score}', False, self.game.display.YELLOW)
                score_rect = score_text.get_rect(center=(self.game.screen_width // 2, y_position))
                self.game.screen.blit(score_text, score_rect)
                y_position += 60

            # Draw return button
            return_text = self.game.display.fonts.button_font.render('Back', False, self.game.display.YELLOW)
            return_button_rect = return_text.get_rect(center=(self.game.screen_width // 2, self.game.screen_height - 100))
            
            # Button hover effect
            mouse_pos = pygame.mouse.get_pos()
            if return_button_rect.collidepoint(mouse_pos):
                return_text = self.game.display.fonts.button_font.render('Back', False, (255, 255, 255))
            
            self.game.screen.blit(return_text, return_button_rect)
            
            pygame.display.flip()
            self.game.clock.tick(60)