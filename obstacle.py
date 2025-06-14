import pygame
from block import Block
from grid import Grid

class Obstacle:
    def __init__(self, x: int = None, y: int = None):

        self.__grid = Grid().create_grid().grid
        self.__blocks_group = pygame.sprite.Group()
        self.__obstacles = []

        if x is not None and y is not None:
            for row in range(len(self.grid)):
                for column in range(len(self.grid[0])):
                    if self.grid[row][column] == 1:
                        pos_x = x + column * 3  #Perguntar ao Alan se é preciso privar tais variaveis
                        pos_y = y + row * 3
                        block = Block(pos_x, pos_y)
                        self.blocks_group.add(block)

    # Setters e Getters
    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, value):
        self.__grid = value

    @property
    def blocks_group(self):
        return self.__blocks_group

    @blocks_group.setter
    def blocks_group(self, value):
        self.__blocks_group = value

    @property
    def obstacles(self):
        return self.__obstacles

    @obstacles.setter
    def obstacles(self, value):
        self.__obstacles = value
    
    def create_obstacles(self, screen_height):
        x = 650

        for i in range(4):
            obstacle = Obstacle(x, screen_height - 200)
            self.obstacles.append(obstacle)
            x += 190
            
        return self.obstacles
    
    def destroy_obstacles(self):
        self.obstacles.clear()
