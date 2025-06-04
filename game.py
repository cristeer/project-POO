import pygame
from random import choice, randint

from spaceship import Spaceship
from obstacle import Obstacle
from grid import Grid
from alien import Alien
from laser import Laser
from mystery_laser import MysteryLaser
from mystery_ship import MysteryShip


class Game:
    def __init__(self, screen_width:int, screen_height:int, offset:int) -> None:
        # Tela, Icones e Som
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.life_icon = pygame.image.load('images/spaceship/spaceship.png')
        self.life_icon = pygame.transform.scale(self.life_icon, (40, 25)) # Tive que criar este ícone em função da transformação do jogador.
        self.explosion_sound = pygame.mixer.Sound('music/explosion.ogg')
        self.mystery_sound = pygame.mixer.Sound('music/laser-zap.mp3')

        # Variáveis da Lógica do Jogo
        self.player_lives = 3
        self.game_state = False
        self.level = 1
        self.transformation_active = False # Transformação do jogador
        self.transformation_time = 0 # Contabilizar o tempo da transformação
        self.mystery_health = 3 # Vida da Nave Misteriosa
        self.mystery_kill = False # Nave Misteriosa Viva (False) ou Morta(True)
        self.aliens_direction = 1 # Velocidade dos Aliens
        
        #Sprites do Jogador
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset))

        # Sprites da Nave Misteriosa
        self.mystery_ship_group = pygame.sprite.GroupSingle()
        self.mystery_ship_lasers_group = pygame.sprite.Group() #teste

        # Sprites dos Aliens
        self.aliens_group = pygame.sprite.Group()
        self.aliens_lasers_group = pygame.sprite.Group()

        # Instaciação dos Obstáculos de Defesa e dos Aliens
        self.obstacles = self.create_obstacles()
        self.aliens = self.create_aliens()

    def create_obstacles(self) -> Obstacle: # Cria as barreiras
        self.grid_instance = Grid()
        self.grid_instance.create_grid()
        obstacle_width = len(self.grid_instance.grid[0]) * 3
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

    def aliens_shoot(self) -> None: # Aliens do bloco atiram
        if self.aliens_group:
            self.rand_alien = choice(self.aliens_group.sprites())
            self.laser_sprite = Laser(self.rand_alien.rect.center, -6, self.screen_height)
            self.aliens_lasers_group.add(self.laser_sprite)

    def create_mystery_ship(self) -> None: # Cria Nave Misteriosa
        self.mystery_ship_group.add(MysteryShip(self.screen_width, self.offset))

    def mystery_shoot(self) -> None: # Nave Misteriosa atira Lasers
        if self.mystery_ship_group:
            position = self.mystery_ship_group.sprite.rect.center
            self.mystery_laser = MysteryLaser(position, -10, self.screen_height)
            self.mystery_ship_lasers_group.add(self.mystery_laser)
            self.mystery_sound.play()

    def check_for_collisions(self) -> None: # Trata todas as colisões
        
        # Colisões da Nave/Jogador: 
        if self.spaceship_group.sprite.laser_group:
            for laser_sprite in self.spaceship_group.sprite.laser_group:
                if pygame.sprite.spritecollide(laser_sprite, self.aliens_group, True):
                    laser_sprite.kill()
                    self.explosion_sound.play()

                elif pygame.sprite.spritecollide(laser_sprite, self.mystery_ship_group, False):
                    self.mystery_health -= 1
                    laser_sprite.kill()
                    if self.mystery_health == 0:
                        self.explosion_sound.play()
                        self.mystery_kill = True
                        self.mystery_ship_group.sprite.kill()
                        self.transformation_active = True
                        self.transformation_time = pygame.time.get_ticks()
            
                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()
                        
        # Colisões dos Lasers dos Aliens
        if self.aliens_group:
            for laser_sprite in self.aliens_lasers_group:
                if pygame.sprite.spritecollide(laser_sprite,self.spaceship_group, False):
                    laser_sprite.kill()

                    if self.transformation_active == False: #Torna o jogador invulnerável quando transformado
                        self.player_lives -= 1

                    if self.player_lives == 0:
                        self.game_over()
                
                for obstacle in self.obstacles: # Aliens destroem as barreiras
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()

            for alien in self.aliens_group:
                for obstacle in self.obstacles:
                    pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
                
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.game_over()

        #Colisões da Nave Misteriosa
        if self.mystery_ship_group:
            for laser_sprite in self.mystery_ship_lasers_group:
                
                if pygame.sprite.spritecollide(laser_sprite, self.spaceship_group, False):
                    laser_sprite.kill() 
                    self.game_over()

                for obstacle in self.obstacles:
                    if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                        laser_sprite.kill()             
                    
    def game_over(self) -> None: # Caso o jogo termine por morte do jogador
        self.game_state = False
        self.level = 1
        self.player_lives = 3
        cur_pos = self.spaceship_group.sprite.rect.midbottom
        self.spaceship_group.empty()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset, cur_pos))
        self.transformation_active = False
        self.transform_time = 0

    def reset_game(self) -> None: # Permite a troca de nível
        self.spaceship_group.sprite.reset()
        self.transformation_active = False
        self.transformation_time = 0
        cur_pos = self.spaceship_group.sprite.rect.midbottom
        self.spaceship_group.empty()
        self.spaceship_group.add(Spaceship(self.screen_width, self.screen_height, self.offset, cur_pos))

        self.aliens_group.empty()
        self.aliens_lasers_group.empty()

        self.mystery_ship_group.empty()
        self.mystery_health = 3

        self.create_aliens()
        self.obstacles = self.create_obstacles()

        self.game_state = True

        pygame.time.set_timer(pygame.USEREVENT + 2, randint(10000, 15000))