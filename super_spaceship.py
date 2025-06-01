from spaceship import Spaceship
import pygame

class SuperSpaceship(Spaceship):

    def __init__(self, width:int, height:int, offset:int, position:int = None):
        super().__init__(width, height, offset, position)

        self.speed = 12
        original_spaceship = pygame.image.load('images/spaceship/spaceship.png')
        self.image = pygame.transform.scale2x(original_spaceship)
        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)
        self.laser_delay = 100
