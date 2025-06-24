import pygame, sys
from button import Button

class Settings:
    def __init__(self, display):
        self.display = display
        self.screen = display.game.screen
        self.fonts = display.fonts
        self.sound = display.game.sound
        
        # Settings state
        self.settings_state = False
        
        # Create buttons
        self.game_volume_up = Button(
            pos=(960, 400),
            text_input='Game Volume +',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        
        self.game_volume_down = Button(
            pos=(960, 500),
            text_input='Game Volume -',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )

        self.music_volume_up = Button(
            pos=(960, 700),
            text_input='Music Volume +',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )

        self.music_volume_down = Button(
            pos=(960, 800),
            text_input='Music Volume -',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        
        self.back_button = Button(
            pos=(960, 950),
            text_input='Back',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        
    def draw_settings(self):
        if not self.settings_state:
            return

        # Draw background
        self.screen.blit(self.display.surfaces.main_bg, (0,0))
        
        # Draw title
        title = self.fonts.title_font.render("SETTINGS", True, self.display.YELLOW)
        title_rect = title.get_rect(center=(960, 200))
        self.screen.blit(title, title_rect)
        
        # Draw volume levels
        game_vol = self.fonts.button_font.render(f"Game Volume: {int(self.sound.game_volume * 100)}%", True, self.display.YELLOW)
        music_vol = self.fonts.button_font.render(f"Music Volume: {int(self.sound.music_volume * 100)}%", True, self.display.YELLOW)
        
        self.screen.blit(game_vol, game_vol.get_rect(center=(960, 300)))
        self.screen.blit(music_vol, music_vol.get_rect(center=(960, 600)))
        
        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in [self.game_volume_up, self.game_volume_down, 
                      self.music_volume_up, self.music_volume_down, 
                      self.back_button]:
            button.changeColor(mouse_pos)
            button.update(self.screen)

        # Controla os eventos do input do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.checkForInput(mouse_pos):
                    self.settings_state = False
                    return
                    
                if self.game_volume_up.checkForInput(mouse_pos):
                    self.sound.game_volume_up()
                    
                elif self.game_volume_down.checkForInput(mouse_pos):
                    self.sound.game_volume_down()
                    
                elif self.music_volume_up.checkForInput(mouse_pos):
                    self.sound.music_volume_up()
                    
                elif self.music_volume_down.checkForInput(mouse_pos):
                    self.sound.music_volume_down()