import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):

    def __init__(self, width:int, height:int, offset:int, position = None) -> None:
        super().__init__()

        # Globais
        self.width = width
        self.height = height
        self.offset = offset
        self.speed = 6

        # Exibir
        self.image = pygame.image.load('images/spaceship/spaceship.png')
        if position:
            self.rect = self.image.get_rect(midbottom = position)
        else:
            self.rect = self.image.get_rect(midbottom = (self.width/2, (self.height - 100)))
        
        #Laser
        self.laser_ready = True
        self.laser_delay = 300
        self.laser_time = 0
        self.laser_group = pygame.sprite.Group()
        self.laser_sound = pygame.mixer.Sound('music/laser.ogg')
        

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x  += self.speed

        elif keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        elif (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and self.laser_ready:
            self.laser_ready = False
            laser = Laser(self.rect.center, 5, self.height)
            self.laser_group.add(laser)
            self.laser_time = pygame.time.get_ticks()
            self.laser_sound.play()


    def constrains(self):
        if self.rect.right > (1415 - self.offset):
            self.rect.right = (1415 - self.offset)

        elif self.rect.left < (485 + self.offset):
            self.rect.left = (485 + self.offset)

    def recharge_laser(self):
        if not self.laser_ready:

            self.current_time = pygame.time.get_ticks()
            
            if self.current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True
    
    def update(self):
        self.laser_group.update()
        self.get_user_input()
        self.constrains()
        self.recharge_laser()

    def reset(self):
        self.rect = self.image.get_rect(midbottom = (self.width/2, self.height - 100))
        self.laser_group.empty()