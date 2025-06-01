import pygame
from laser import Laser

class MysteryLaser(Laser, pygame.sprite.Sprite):

    def __init__(self, position, speed, height):
        super().__init__(position, speed, height)
        RED = (255, 0, 0)
        self.speed = speed
        self.height = height

        self.image = pygame.Surface((32, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center = position)

    def destroy(self):
        if self.rect.y + 60 > self.height:
            self.kill()
    
    def laser_move(self):
        self.rect.y -= self.speed

    def update(self):
        self.laser_move()
        self.destroy()