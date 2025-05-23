import pygame, sys
from spaceship import Spaceship
from game import Game

pygame.init()

# Global Variables
GREY = (29, 29, 27)
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

SHOOT_LASER = pygame.USEREVENT + 1
pygame.time.set_timer(SHOOT_LASER, 300)

# Setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders')

clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == SHOOT_LASER:
            game.aliens_shoot()
        
    # Atualizar
    game.spaceship_group.update()
    game.aliens_lasers_group.update()
    game.move_aliens()

    # Exibir
    screen.fill(GREY)
    game.spaceship_group.draw(screen)
    game.spaceship_group.sprite.laser_group.draw(screen)
    game.aliens_lasers_group.draw(screen)

    for obstacle in game.obstacles:
        obstacle.blocks_group.draw(screen)

    game.aliens_group.draw(screen)
        
    pygame.display.update()
    clock.tick(60)

