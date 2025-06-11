import pygame
from block import Block
from grid import Grid

class Obstacle:
    def __init__(self, x: int = None, y: int = None):
        self.grid_instance = Grid()
        self.grid_instance.create_grid()
        self.grid = self.grid_instance.grid
        self.blocks_group = pygame.sprite.Group()

        if x is not None and y is not None:
            for row in range(len(self.grid)):
                for column in range(len(self.grid[0])):
                    if self.grid[row][column] == 1:
                        pos_x = x + column * 3
                        pos_y = y + row * 3
                        block = Block(pos_x, pos_y)
                        self.blocks_group.add(block)
    
    def create_obstacles(self, screen_height):
        obstacles = []
        x = 650

        for i in range(4):
            obstacle = Obstacle(x, screen_height - 200)
            obstacles.append(obstacle)
            x += 190
            
        return obstacles
