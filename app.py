import pygame, sys
from random import randint

from spaceship import Spaceship
from super_spaceship import SuperSpaceship
from game import Game

pygame.init()

# Global Variables
GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

SCREEN_WIDTH = pygame.display.Info().current_w
SCREEN_HEIGHT = pygame.display.Info().current_h
OFFSET = 50

SHOOT_LASER = pygame.USEREVENT + 1
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(MYSTERYSHIP_SPAWN, randint(10000, 15000))

SHOOT_MYSTERY_LASER = pygame.USEREVENT + 3
pygame.time.set_timer(SHOOT_MYSTERY_LASER, 2000)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET), pygame.FULLSCREEN)
pygame.display.set_caption('Space Invaders')

font = pygame.font.Font('fonts/monogram.ttf', 50)
clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

# UI

game_over_surface = font.render('GAME OVER', False, YELLOW)
score_text_surface = font.render('SCORE', False, YELLOW)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SHOOT_LASER and game.game_state:
            game.aliens_shoot()

        if event.type == SHOOT_MYSTERY_LASER and game.game_state:
            game.mystery_shoot()

        if event.type == MYSTERYSHIP_SPAWN and game.game_state and len(game.mystery_ship_group) == 0:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP_SPAWN, 0)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.game_state == False:
            game.reset_game()

    # Atualizar
    if game.game_state == True:
        game.spaceship_group.update()
        game.aliens_lasers_group.update()
        game.mystery_ship_group.update()
        game.mystery_ship_lasers_group.update()
        game.move_aliens()
        game.check_for_collisions()

        if len(game.aliens_group) == 0 and len(game.mystery_ship_group) == 0:
            game.level += 1
            game.reset_game()

    if game.transformation_active and game.mystery_kill:
        cur_pos = game.spaceship_group.sprite.rect.midbottom
        game.spaceship_group.empty()
        super_spaceship = SuperSpaceship(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET, position = cur_pos)
        game.spaceship_group.add(super_spaceship)
        super_spaceship.laser_ready = True
        super_spaceship.laser_time = pygame.time.get_ticks()
        game.mystery_kill = False

    if game.transformation_active:
        now = pygame.time.get_ticks()
        if now - game.transformation_time >= 10000:
            cur_pos = game.spaceship_group.sprite.rect.midbottom
            game.spaceship_group.empty()
            normal_spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET, cur_pos)
            normal_spaceship.laser_ready = True
            normal_spaceship.laser_time = pygame.time.get_ticks()
            game.spaceship_group.add(normal_spaceship)
            game.transformation_active = False
        
    # Exibir Interface de Usuário
    
    screen.fill(GREY)

    # Exibe o menu de vidas se houver jogo rodando, caso contrário, exibe o game over
    if game.game_state:
        level_surface = font.render(f'LEVEL {game.level:02}', False, YELLOW)
        screen.blit(level_surface, (1225, 1020, 50, 50))
        x = 520
        for life in range(game.player_lives):
            screen.blit(game.life_icon, (x, 1020))
            x += 50

        screen.blit(score_text_surface, (520, 25, 50, 50))
        formatted_score = str(game.score).zfill(6)
        score_surface = font.render(formatted_score, False, YELLOW)
        screen.blit(score_surface, (520, 50, 50, 50))  
    
    else:
        screen.blit(game_over_surface, (1225, 1020, 50, 50))

    pygame.draw.rect(screen, YELLOW, (485, 10, 950, 1060), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (505, 1010), (1415, 1010), 3)

    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    game.aliens_lasers_group.draw(screen)
    game.mystery_ship_lasers_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    game.aliens_group.draw(screen)
    game.mystery_ship_group.draw(screen)
        
    pygame.display.update()
    clock.tick(60)

