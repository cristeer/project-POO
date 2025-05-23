import pygame
from random import choice

from spaceship import Spaceship
from obstacle import Obstacle
from grid import Grid
from alien import Alien
from laser import Laser


class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height))
        
        self.aliens_group = pygame.sprite.Group()
        self.aliens_lasers_group = pygame.sprite.Group()
        self.aliens_direction = 1
        
        self.obstacles = self.create_obstacles()
        self.aliens = self.create_aliens()

    def create_obstacles(self) -> Obstacle: # Cria as barreiras
        grid_instance = Grid()
        grid_instance.create_grid()
        obstacle_width = len(grid_instance.grid[0]) * 3
        gap = (self.screen_width - (4 * obstacle_width)) / 5
        obstacles = []
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            obstacle = Obstacle(offset_x, self.screen_height - 100)
            obstacles.append(obstacle)
        return obstacles
    
    def create_aliens(self) -> None: # Cria os aliens
        for row in range(5):
            for col in range(11):
                self.x = 75 + col * 55
                self.y = 110 + row * 55

                if row == 0:
                    self.alien_type = 3
                elif row in (1, 2):
                    self.alien_type = 2
                else:
                    self.alien_type = 1
                    
                self.alien_inst = Alien(self.alien_type, self.x, self.y)
                self.aliens_group.add(self.alien_inst)

    def move_aliens(self) -> None: #Move os aliens lateralmente
        self.aliens_group.update(self.aliens_direction)

        for alien in self.aliens_group:
            if alien.rect.right >= self.screen_width:
                self.aliens_direction = -1
                self._move_aliens_down_(2)
                break
            elif alien.rect.left <= 0:
                self.aliens_direction = 1
                self._move_aliens_down_(2)
                break
    
    def _move_aliens_down_(self, distance:int) -> None: # Método protegido que move os aliens para baixo
        if self.aliens_group:
            for alien in self.aliens_group:
                alien.rect.y += distance

    def aliens_shoot(self) -> None:
        if self.aliens_group:
            self.rand_alien = choice(self.aliens_group.sprites())
            self.laser_sprite = Laser(self.rand_alien.rect.center, -6, self.screen_height)
            self.aliens_lasers_group.add(self.laser_sprite)