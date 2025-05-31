import pygame
from random import choice

from spaceship import Spaceship
from obstacle import Obstacle
from grid import Grid
from alien import Alien
from laser import Laser
from mystery_ship import MysteryShip


class Game:
    def __init__(self, screen_width:int, screen_height:int, offset:int) -> None:
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.player_lives = 3
        self.game_state = False

        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset))

        self.mystery_ship_group = pygame.sprite.GroupSingle()
        
        self.aliens_group = pygame.sprite.Group()
        self.aliens_lasers_group = pygame.sprite.Group()
        self.aliens_direction = 1
        
        self.obstacles = self.create_obstacles()
        self.aliens = self.create_aliens()

    def create_obstacles(self) -> Obstacle: # Cria as barreiras
        grid_instance = Grid()
        grid_instance.create_grid()
        obstacle_width = len(grid_instance.grid[0]) * 3
        gap = ((self.screen_width + self.offset) - (4 * obstacle_width)) / 5
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
                    
                self.alien_inst = Alien(self.alien_type, (self.x + self.offset/2), self.y)
                self.aliens_group.add(self.alien_inst)

    def move_aliens(self) -> None: #Move os aliens lateralmente
        self.aliens_group.update(self.aliens_direction)

        for alien in self.aliens_group:
            if alien.rect.right >= (self.screen_width + self.offset/2):
                self.aliens_direction = -1
                self._move_aliens_down_(2)
                break
            elif alien.rect.left <= self.offset/2:
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

    def create_mystery_ship(self) -> None:
        self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

    def check_for_collisions(self) -> None:
        # Colisões da Nave: 
        if self.spaceship_group.sprite.laser_group:
            for laser_sprite in self.spaceship_group.sprite.laser_group:
                if pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True):
                    laser_sprite.kill()
                elif pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, True):
                    laser_sprite.kill()
            
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
                        
        # Colisões dos Lasers dos Aliens
        if self.aliens_group:
            for laser_sprite in self.aliens_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite,self.spaceship_group, False):
                    laser_sprite.kill()
                    self.player_lives -= 1
                    if self.player_lives == 0:
                        self.game_over()
                
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()

    def game_over(self):
        self.game_state = False

    def reset_game(self):
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.aliens_lasers_group.empty()
        self.mystery_ship_group.empty()

        self.create_aliens()
        self.obstacles = self.create_obstacles()

        self.game_state = True