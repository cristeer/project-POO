import pygame

class Alien(pygame.sprite.Sprite):
    def __init__(self, alien_type, x, y):
        super().__init__()
        self.alien_type = alien_type
        path = f"images/aliens/alien_{self.alien_type}.png"
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(topleft = (x, y))
    
    def update(self, direction:int) -> None:
        self.rect.x += direction