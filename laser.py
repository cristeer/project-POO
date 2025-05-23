import pygame

class Laser(pygame.sprite.Sprite):

    def __init__(self, position:int, speed:int, height:int):
        super().__init__()
        YELLOW = (243, 216, 63)
        self.speed = speed
        self.height = height

        self.image = pygame.Surface((8, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center = position)

    def destroy(self):
        if self.rect.y + 20 > self.height:
            self.kill()
    
    def laser_move(self):
        self.rect.y -= self.speed

    def update(self):
        self.laser_move()
        self.destroy()