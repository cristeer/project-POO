import pygame
import os

class Sound:
    def __init__(self):
        pygame.mixer.init()
        
        # Tentar carregar sons reais, com fallback para sons dummy
        try:
            self.explosion_sound = pygame.mixer.Sound('music/explosion.ogg')
            self.explosion_sound.set_volume(0.3)
        except:
            self.explosion_sound = pygame.mixer.Sound(buffer=b'\x00' * 1024)
            self.explosion_sound.set_volume(0.3)
            
        try:
            self.mystery_sound = pygame.mixer.Sound('music/laser-zap.mp3')
            self.explosion_sound.set_volume(0.1)
        except:
            self.mystery_sound = pygame.mixer.Sound(buffer=b'\x00' * 1024)
            self.mystery_sound.set_volume(0.1)
            
        try:
            self.laser_sound = pygame.mixer.Sound('music/laser.ogg')
            self.explosion_sound.set_volume(0.3)
        except:
            self.laser_sound = pygame.mixer.Sound(buffer=b'\x00' * 1024)
            self.laser_sound.set_volume(0.3)
            
        try:
            self.bg_music = pygame.mixer.Sound('music/explosion.ogg')
            self.explosion_sound.set_volume(0.1)
        except:
            self.bg_music = pygame.mixer.Sound(buffer=b'\x00' * 1024)
            self.bg_music.set_volume(0.3)
        
    def load_music(self):
            pygame.mixer.music.load('music/music.ogg')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            