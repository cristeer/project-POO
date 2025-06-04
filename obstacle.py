import pygame
from block import Block
from grid import Grid

# Cria os obstaculos
class Obstacle:
    def __init__(self, x, y):
        self.grid_instance = Grid()
        self.grid_instance.create_grid()
        self.grid = self.grid_instance.grid
        self.blocks_group = pygame.sprite.Group()

        for row in range(len(self.grid)):
            for column in range(len(self.grid[0])):
                if self.grid[row][column] == 1:
                    pos_x = x + column * 3
                    pos_y = y + row * 3
                    self.block = Block(pos_x, pos_y)
                    self.blocks_group.add(self.block)

