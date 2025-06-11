import pygame

class Sound:
    def __init__(self):

        pygame.mixer.init()
        
        self.explosion_sound = pygame.mixer.Sound('music/explosion.ogg')
        
        self.mystery_sound = pygame.mixer.Sound('music/laser-zap.mp3')    
        
        self.laser_sound = pygame.mixer.Sound('music/laser.ogg')
                
        self.bg_music = pygame.mixer.Sound('music/explosion.ogg')

    def loop_music(self):
            pygame.mixer.music.load('music/music.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
        