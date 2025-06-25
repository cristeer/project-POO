import pygame, sys
from button import Button

class Settings:
    def __init__(self, display):
        self.__display = display
        self.__screen = display.game.screen
        self.__fonts = display.fonts
        self.__sound = display.game.sound

        # Configuração Estado
        self.__settings_state = False
        
        # Botões
        self.__game_volume_up = Button(
            pos = (960, 400),
            text_input = 'Game Volume +',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )
        
        self.__game_volume_down = Button(
            pos = (960, 500),
            text_input = 'Game Volume -',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.__music_volume_up = Button(
            pos = (960, 700),
            text_input = 'Music Volume +',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

        self.__music_volume_down = Button(
            pos = (960, 800),
            text_input='Music Volume -',
            text_font=self.fonts.button_font,
            base_color="White",
            hovering_color="#b68f40"
        )
        
        self.__back_button = Button(
            pos = (960, 950),
            text_input = 'Back',
            text_font = self.fonts.button_font,
            base_color = "White",
            hovering_color = "#b68f40"
        )

    # Setters e Getters
    @property
    def display(self):
        return self.__display

    @display.setter
    def display(self, value):
        self.__display = value

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
    def sound(self):
        return self.__sound

    @sound.setter
    def sound(self, value):
        self.__sound = value
    
    @property
    def settings_state(self):
        return self.__settings_state

    @settings_state.setter
    def settings_state(self, value):
        self.__settings_state = value

    @property
    def game_volume_up(self):
        return self.__game_volume_up

    @game_volume_up.setter
    def game_volume_up(self, value):
        self.__game_volume_up = value

    @property
    def game_volume_down(self):
        return self.__game_volume_down

    @game_volume_down.setter
    def game_volume_down(self, value):
        self.__game_volume_down = value

    @property
    def music_volume_up(self):
        return self.__music_volume_up

    @music_volume_up.setter
    def music_volume_up(self, value):
        self.__music_volume_up = value

    @property
    def music_volume_down(self):
        return self.__music_volume_down

    @music_volume_down.setter
    def music_volume_down(self, value):
        self.__music_volume_down = value

    @property
    def back_button(self):
        return self.__back_button

    @back_button.setter
    def back_button(self, value):
        self.__back_button = value
    
    # Métodos
    def draw_settings(self):
        if not self.settings_state:
            return

        # Draw background
        self.screen.blit(self.display.surfaces.main_bg, (0,0))
        self.screen.blit(self.display.surfaces.settings_title, self.display.surfaces.settings_title_rect)
        
        # # Draw volume levels
        self.game_vol_text = self.fonts.button_font.render(f"Game Volume: {int(self.sound.game_volume * 100)}%", True, self.display.YELLOW)
        self.music_vol_text = self.fonts.button_font.render(f"Music Volume: {int(self.sound.music_volume * 100)}%", True, self.display.YELLOW)
        
        self.screen.blit(self.game_vol_text, self.game_vol_text.get_rect(center = (960, 300)))
        self.screen.blit(self.music_vol_text, self.music_vol_text.get_rect(center = (960, 600)))
        
        # Draw buttons
        mouse_pos = pygame.mouse.get_pos()
        for button in [self.game_volume_up, self.game_volume_down, 
                      self.music_volume_up, self.music_volume_down, 
                      self.back_button]:
            button.change_color(mouse_pos)
            button.update(self.screen)

        # Controla os eventos do input do jogador
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.check_for_input(mouse_pos):
                    self.settings_state = False
                    return
                    
                if self.game_volume_up.check_for_input(mouse_pos):
                    self.sound.game_volume_up()
                    
                elif self.game_volume_down.check_for_input(mouse_pos):
                    self.sound.game_volume_down()
                    
                elif self.music_volume_up.check_for_input(mouse_pos):
                    self.sound.music_volume_up()
                    
                elif self.music_volume_down.check_for_input(mouse_pos):
                    self.sound.music_volume_down()