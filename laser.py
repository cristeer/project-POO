import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self, position: tuple = None, speed: int = None, height: int = None):
        super().__init__()
        YELLOW = (243, 216, 63)
        self.speed = speed or 5
        self.height = height or 800

        self.image = pygame.Surface((8, 20))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center = position or (0, 0))

    def destroy(self) -> None:
        if self.rect.y + 20 > self.height or self.rect.y < 0:
            self.kill()
    
    def laser_move(self) -> None:
        self.rect.y -= self.speed

    def update(self) -> None:
        self.laser_move()
        self.destroy()
