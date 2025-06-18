import pygame, json, sys, os
from random import randint

from spaceship import Spaceship
from obstacle import Obstacle
from alien import Alien
from mystery_ship import MysteryShip
from display import Display
from sound import Sound
from black_hole import BlackHole
from save import Save

class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.sound = Sound()
        self.sound.loop_music()

        # Variáveis da Lógica do Jogo
        self.game_state = False
        self.level = 1
        self.score = 0
        self.highscore = 0
        self.load_highscore()
        self.clock = pygame.time.Clock()

        # Configurações da tela
        self.screen_width = pygame.display.Info().current_w
        self.screen_height = pygame.display.Info().current_h
        self.offset = 50

        # Setup
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Space Invaders')
        
        # Eventos Periódicos
        self.SHOOT_LASER = pygame.USEREVENT + 1
        pygame.time.set_timer(self.SHOOT_LASER, 300)
        
        self.MYSTERYSHIP_SPAWN = pygame.USEREVENT + 2
        pygame.time.set_timer(self.MYSTERYSHIP_SPAWN, randint(10000, 15000))

        self.SHOOT_MYSTERY_LASER = pygame.USEREVENT + 3
        pygame.time.set_timer(self.SHOOT_MYSTERY_LASER, 2000)

        self.BLACK_HOLE_SPAWN = pygame.USEREVENT + 4
        pygame.time.set_timer(self.BLACK_HOLE_SPAWN, randint(10000, 15000))

        # Objetos
        self.spaceship = Spaceship(self.screen_width, self.screen_height, self.offset)
        self.mystery_ship = MysteryShip(self.screen_width, self.screen_height, self.offset, self.spaceship)
        self.alien = Alien(self.offset)
        self.obstacle = Obstacle()
        self.obstacles = []
        self.black_hole = BlackHole(self.spaceship, x = 400, y = 750, offset = 50) #corrigir, não está dinamizado 
        
        self.display = Display(self)
        self.save = Save(self)

    def check_for_collisions(self) -> None:
        # Colisões dos lasers do jogador
        for laser_sprite in self.spaceship.laser_group:
            # Colisão com aliens
            aliens_hit = pygame.sprite.spritecollide(laser_sprite, self.alien.aliens_group, True)
            if aliens_hit:
                for alien in aliens_hit:
                    self.score += alien.alien_type * 100
                    self.check_for_highscore()
                    laser_sprite.kill()
                self.sound.explosion_sound.play()
                
            # Colisão com nave misteriosa
            if pygame.sprite.spritecollide(laser_sprite, self.mystery_ship.mystery_ship_group, False):
                self.mystery_ship.mystery_health -= 1
                laser_sprite.kill()
                
                if self.mystery_ship.mystery_health == 0:
                    self.score += 500
                    self.check_for_highscore()
                    self.sound.explosion_sound.play()
                    self.mystery_ship.mystery_kill = True
                    self.mystery_ship.mystery_ship_group.sprite.kill()
                    self.spaceship.transformation_active = True
                    self.spaceship.transformation_time = pygame.time.get_ticks()

            # Colisão com obstáculos
            for obstacle in self.obstacles:
                if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                    laser_sprite.kill()

        # Colisões dos lasers dos aliens
        for laser_sprite in self.alien.aliens_lasers_group:
            if pygame.sprite.spritecollide(laser_sprite, self.spaceship.spaceship_group, False):
                laser_sprite.kill()
                if not self.spaceship.transformation_active:
                    self.spaceship.player_lives -= 1
                if self.spaceship.player_lives == 0:
                    self.game_over()
            for obstacle in self.obstacles:
                if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                    laser_sprite.kill()

        # Colisão dos aliens com obstáculos e nave
        for alien in self.alien.aliens_group:
            for obstacle in self.obstacles:
                pygame.sprite.spritecollide(alien, obstacle.blocks_group, True)
            if pygame.sprite.spritecollide(alien, self.spaceship.spaceship_group, False):
                self.game_over()

        # Colisões dos lasers da nave misteriosa
        for laser_sprite in self.mystery_ship.mystery_ship_lasers_group:
            if pygame.sprite.spritecollide(laser_sprite, self.spaceship.spaceship_group, False):
                laser_sprite.kill()
                if not self.spaceship.transformation_active:
                    self.spaceship.player_lives -= 1
                if self.spaceship.player_lives == 0:
                    self.game_over()
            for obstacle in self.obstacles:
                if pygame.sprite.spritecollide(laser_sprite, obstacle.blocks_group, True):
                    laser_sprite.kill()

    def game_over(self) -> None:
        self.game_state = False
        self.level = 1
        self.display.surfaces.level_surface = self.display.fonts.font.render(f'LEVEL {self.level:02}', False, self.display.YELLOW)
        self.spaceship.player_lives = 3 
        self.spaceship.transformation_active = False
        self.spaceship.transformation_time = 0
        self.score = 0
        self.black_hole.destroy_black_hole()
        if os.path.exists('save_game.json'):
            os.remove('save_game.json')

    def reset_game(self) -> None:
        self.spaceship.reset()
        self.spaceship.transformation_active = False 
        self.spaceship.transformation_time = 0

        self.spaceship.spaceship_group.empty() # implementar destrutor
        self.spaceship.spaceship_group.add(self.spaceship)

        self.alien.aliens_group.empty() # implementar no destrutor
        self.alien.aliens_lasers_group.empty()
        self.alien.aliens_direction = 1

        self.mystery_ship.mystery_ship_group.empty() #implementar no destrutor
        self.mystery_ship.mystery_health = 3
        self.mystery_ship.mystery_kill = False

        self.black_hole.destroy_black_hole()

        self.spaceship.spaceship_group.empty()
        self.spaceship.spaceship_group.add(self.spaceship)

        self.alien.aliens_group.empty()
        self.alien.aliens_lasers_group.empty()
        self.alien.aliens_direction = 1

        self.mystery_ship.mystery_ship_group.empty()
        self.mystery_ship.mystery_health = 3
        self.mystery_ship.mystery_kill = False

        self.alien.create_aliens(self.offset)
        self.obstacles = self.obstacle.create_obstacles(self.screen_height)

        self.game_state = True

        pygame.time.set_timer(self.MYSTERYSHIP_SPAWN, randint(10000, 15000))
        pygame.time.set_timer(self.BLACK_HOLE_SPAWN, randint(10000, 15000))

    def check_for_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score

            #Salva o highscore em um arquivo JSON
            with open('highscore.json', 'w') as file: 
                json.dump(self.highscore, file)
    
    # Carrega o highscore do arquivo JSON
    def load_highscore(self):
        try: #tenta abrir highscore.json para leitura
            with open('highscore.json', 'r') as file:
                self.highscore = int(json.load(file)) #lê e converte o valor para int
        except FileNotFoundError: #se nao existir o arquivo, define o highscore como 0
            self.highscore = 0


    def run_game(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.save.save_game()
                    pygame.quit()
                    sys.exit()

                if event.type == self.SHOOT_LASER and self.game_state:
                    self.alien.aliens_shoot(self.screen_height)

                if event.type == self.SHOOT_MYSTERY_LASER and self.game_state:
                    self.mystery_ship.mystery_shoot()

                if event.type == self.BLACK_HOLE_SPAWN:
                    self.black_hole.create_black_hole()
                    pygame.time.set_timer(self.BLACK_HOLE_SPAWN, 0)

                if event.type == self.MYSTERYSHIP_SPAWN and self.game_state and len(self.mystery_ship.mystery_ship_group) == 0:
                    self.mystery_ship.create_mystery_ship()
                    pygame.time.set_timer(self.MYSTERYSHIP_SPAWN, 0)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE] and self.game_state == False:
                    self.reset_game()
                    
                if keys[pygame.K_l] and self.game_state == False: 
                    if self.save.load_game():
                        self.game_state = True #concertar depois pra ser acessado no menu

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE and self.game_state:
                    event_type = self.display.pause_menu()
                
                    if event_type == 'menu':
                        self.game_state = False

            # Atualizar
            if self.game_state == True:
                self.spaceship.spaceship_group.update()
                self.spaceship.laser_group.update()
                self.alien.aliens_group.update(self.alien.aliens_direction)
                self.alien.aliens_lasers_group.update()
                self.mystery_ship.mystery_ship_group.update()
                self.mystery_ship.mystery_ship_lasers_group.update()
                self.black_hole.update()
                self.alien.move_aliens(self.offset)
                self.check_for_collisions()

                if len(self.alien.aliens_group) == 0:
                    self.level += 1
                    self.display.surfaces.level_surface = self.display.fonts.font.render(f'LEVEL {self.level:02}', False, self.display.YELLOW)
                    self.reset_game()

            if self.spaceship.transformation_active and self.mystery_ship.mystery_kill:
                self.spaceship.super_spaceship()
                self.mystery_ship.mystery_kill = False

            if self.spaceship.transformation_active:
                current_time = pygame.time.get_ticks()
                if current_time - self.spaceship.transformation_time >= 10000:
                    self.spaceship.reset_transformation()

            self.display.draw_game()
            pygame.display.update()
            self.clock.tick(60)