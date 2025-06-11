import pygame
from laser import Laser

class MysteryLaser(Laser):
    def __init__(self, position: tuple, speed: int, height: int, spaceship_group):
        super().__init__(position, speed, height)
        RED = (255, 0, 0)
        self.speed = speed
        self.height = height
        self.spaceship_group = spaceship_group

        self.image = pygame.Surface((32, 80))
        self.image.fill(RED)
        self.rect = self.image.get_rect(center=position)

    def destroy(self):
        if self.rect.y + 60 > self.height or self.rect.y < 0:
            self.kill()
    
    def laser_move(self):
        self.rect.y -= self.speed
        if self.spaceship_group.sprite:
            self.rect.x = self.spaceship_group.sprite.rect.x

    def update(self):
        self.laser_move()
        self.destroy()
