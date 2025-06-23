import pygame

class Sound:
    def __init__(self):

        pygame.mixer.init()
        
        self.__explosion_sound = pygame.mixer.Sound('music/explosion.ogg')
        self.__mystery_sound = pygame.mixer.Sound('music/laser-zap.mp3')    
        self.__laser_sound = pygame.mixer.Sound('music/laser.ogg')
        self.__bg_music = pygame.mixer.Sound('music/explosion.ogg')

        self.__game_volume = 0.5
        self.__music_volume = 0.5

        self.laser_sound.set_volume(self.game_volume)
        self.mystery_sound.set_volume(self.game_volume)
        self.explosion_sound.set_volume(self.game_volume)


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

    def loop_music(self):
            pygame.mixer.music.load('music/music.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(self.music_volume)

    def game_volume_up(self):
        if self.game_volume < 1: 
            self.game_volume += 0.1
            # Update all game sound volumes
            self.explosion_sound.set_volume(self.game_volume)
            self.mystery_sound.set_volume(self.game_volume)
            self.laser_sound.set_volume(self.game_volume)
            self.bg_music.set_volume(self.game_volume)

    def game_volume_down(self):
        if self.game_volume > 0.1:
             self.game_volume -= 0.1
             # Update all game sound volumes
             self.explosion_sound.set_volume(self.game_volume)
             self.mystery_sound.set_volume(self.game_volume)
             self.laser_sound.set_volume(self.game_volume)
             self.bg_music.set_volume(self.game_volume)

    def music_volume_up(self):
        if self.music_volume < 1: 
            self.music_volume += 0.1  
            pygame.mixer.music.set_volume(self.music_volume)

    def music_volume_down(self):
        if self.music_volume > 0.1:
            self.music_volume -= 0.1  
            pygame.mixer.music.set_volume(self.music_volume)