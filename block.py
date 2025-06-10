import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((3, 3))
        self.image.fill((243, 216, 63))
        self.rect = self.image.get_rect(topleft=(x, y))
