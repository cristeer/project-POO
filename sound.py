import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()

        # Variáveis de Controle
        self.__game_volume = 0.5
        self.__music_volume = 0.5
        
        # Faixas de Áudio
        self.__explosion_sound = pygame.mixer.Sound('music/explosion.ogg')
        self.__mystery_sound = pygame.mixer.Sound('music/laser-zap.mp3')    
        self.__laser_sound = pygame.mixer.Sound('music/laser.ogg')
        self.__bg_music = pygame.mixer.Sound('music/music.ogg')

    # Setters e Getters
    @property
    def explosion_sound(self):
        return self.__explosion_sound

    @explosion_sound.setter
    def explosion_sound(self, value):
        self.__explosion_sound = value

    @property
    def mystery_sound(self):
        return self.__mystery_sound

    @mystery_sound.setter
    def mystery_sound(self, value):
        self.__mystery_sound = value

    @property
    def laser_sound(self):
        return self.__laser_sound

    @laser_sound.setter
    def laser_sound(self, value):
        self.__laser_sound = value

    @property
    def bg_music(self):
        return self.__bg_music

    @bg_music.setter
    def bg_music(self, value):
        self.__bg_music = value

    @property
    def game_volume(self):
        return self.__game_volume

    @game_volume.setter
    def game_volume(self, value):
        self.__game_volume = value

    @property
    def music_volume(self):
        return self.__music_volume

    @music_volume.setter
    def music_volume(self, value):
        self.__music_volume = value

    # Métodos
    def loop_music(self) -> None: # Faz com que a música toque indefinidamente
        self.bg_music.play(-1)

    def set_game_volume(self, volume: float) -> None: # Altera os sons do jogo
        self.game_volume = max(0.0, min(1.0, volume))
        self.explosion_sound.set_volume(self.game_volume)
        self.laser_sound.set_volume(self.game_volume)
        self.mystery_sound.set_volume(self.game_volume)

    def set_music_volume(self, volume: float) -> None: # Altera a Música de Fundo
        self.music_volume = max(0.0, min(1.0, volume))
        self.bg_music.set_volume(self.music_volume)
        
    def game_volume_up(self) -> None: # Aumentar volume do Jogo (Lasers, Explosões, etc)
        self.set_game_volume(self.game_volume + 0.1)

    def game_volume_down(self) -> None: # Reduzir volume do jogo
        self.set_game_volume(self.game_volume - 0.1)

    def music_volume_up(self) -> None: # Aumentar Música
        self.set_music_volume(self.music_volume + 0.1)

    def music_volume_down(self) -> None: # Reduzir Música
        self.set_music_volume(self.music_volume - 0.1)