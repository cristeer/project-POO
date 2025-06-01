import pygame, sys
from random import randint

from spaceship import Spaceship
from game import Game

pygame.init()

# Global Variables
GREY = (29, 29, 27)
YELLOW = (243, 216, 63)

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

SHOOT_LASER = pygame.USEREVENT + 1
pygame.time.set_timer(SHOOT_LASER, 300)

MYSTERYSHIP_SPAWN = pygame.USEREVENT + 2
pygame.time.set_timer(MYSTERYSHIP_SPAWN, randint(10000, 15000))

SHOOT_MYSTERY_LASER = pygame.USEREVENT + 3
pygame.time.set_timer(SHOOT_MYSTERY_LASER, 1000)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2*OFFSET))
pygame.display.set_caption('Space Invaders')

font = pygame.font.Font('fonts/monogram.ttf', 50)
clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT, OFFSET)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

# UI

game_over_surface = font.render('GAME OVER', False,YELLOW)

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

        if event.type == MYSTERYSHIP_SPAWN and game.game_state and game.mystery_counter == 0:
            game.create_mystery_ship()
            pygame.time.set_timer(MYSTERYSHIP_SPAWN, 0)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and game.game_state == False:
            game.reset_game()

    # Atualizar
    if game.game_state:
        game.spaceship_group.update()
        game.aliens_lasers_group.update()
        game.mystery_ship_group.update()
        game.mystery_ship_lasers_group.update()
        game.move_aliens()
        game.check_for_collisions()

        if len(game.aliens_group) == 0 and len(game.mystery_ship_group) == 0:
            game.level += 1
            game.reset_game()

    # Exibir Interface de Usuário
    
    screen.fill(GREY)

    if game.game_state:
        level_surface = font.render(f'LEVEL {game.level:02}', False, YELLOW)
        screen.blit(level_surface, (570, 740, 50, 50))
        x = 50
        for life in range(game.player_lives):
            screen.blit(game.spaceship_group.sprite.image, (x, 745))
            x += 50
            
    else:
        screen.blit(game_over_surface, (570, 740, 50, 50))




    pygame.draw.rect(screen, YELLOW, (10, 10, 780, 780), 2, 0, 60, 60, 60, 60)
    pygame.draw.line(screen, YELLOW, (25, 730), (775, 730), 3)

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

