import json

class Save:

    def __init__(self, game):
        
        self.__game = game
        self.__mystery_ship_position = None
        self.__spaceship_position = None
        self.__game_data = {}

    @property
    def game(self):
        return self.__game
    
    @game.setter
    def game(self, value):
        self.__game = value
    
    @property
    def game_data(self):
        return self.__game_data
    
    @game_data.setter
    def game_data(self, value):
        self.__game_data = value

    @property
    def mystery_ship_position(self):
        return self.__mystery_ship_position
    
    @mystery_ship_position.setter
    def mystery_ship_position(self, value):
        self.__mystery_ship_position = value

    @property
    def spaceship_position(self):
        return self.__spaceship_position
    
    @spaceship_position.setter
    def spaceship_position(self, value):
        self.__spaceship_position = value

    def inicializar_game_data(self):
        if self.game.spaceship.spaceship_group:
            self.spaceship_position = list(self.game.spaceship.spaceship_group.sprite.rect.topleft)

        #if self.game.mystery_ship.mystery_ship_group:
        #    self.mystery_ship_position = list(self.game.mystery_ship.mystery_ship_group.sprite.rect.topleft)
#

        # Create game data dictionary
        self.game_data = {
            'level': self.game.level,
            'score': self.game.score,
            'highscore': self.game.highscore,
            'lives': self.game.spaceship.player_lives,
            #'transformation_active': self.game.spaceship.transformation_active,
            #'transformation_time': self.game.spaceship.transformation_time,
            #'mystery_health': self.game.mystery_ship.mystery_health,
            #'mystery_kill': self.game.mystery_ship.mystery_kill,
            #'mystery_active': len(self.game.mystery_ship.mystery_ship_group) > 0,
            #'mystery_ship_position': self.mystery_ship_position,
            'spaceship_position': self.spaceship_position
        }

    def save_game(self) -> None:
        # Refresh game data before saving
        self.inicializar_game_data()
        
        # Save to file
        with open('save_game.json', 'w') as file:
            json.dump(self.game_data, file)
        
    def load_game(self):
        try:
            with open('save_game.json', 'r') as file:
                self.game_data = json.load(file)

                # Load game state
                self.game.level = self.game_data['level']
                self.game.display.surfaces.level_surface = self.game.display.fonts.font.render(
                    f'LEVEL {self.game.level:02}', False, self.game.display.YELLOW)
                self.game.score = self.game_data['score']
                self.game.highscore = self.game_data['highscore']
                
                # Load player state
                self.game.spaceship.player_lives = self.game_data['lives']
                #self.game.spaceship.transformation_active = self.game_data['transformation_active']
                #self.game.spaceship.transformation_time = self.game_data['transformation_time']
                
                # Load mystery ship state
                #self.game.mystery_ship.mystery_health = self.game_data['mystery_health']
                #self.game.mystery_ship.mystery_kill = self.game_data['mystery_kill']

                # Reset and recreate game objects
                self.game.mystery_ship.mystery_ship_lasers_group.empty()
                self.game.spaceship.laser_group.empty()
                self.game.alien.aliens_group.empty()
                self.game.alien.aliens_lasers_group.empty()
                self.game.alien.create_aliens(self.game.offset)
                self.game.obstacles = self.game.obstacle.create_obstacles(self.game.screen_height)

                # Restore spaceship position
                self.game.spaceship.spaceship_group.empty()
                self.game.spaceship.spaceship_group.add(self.game.spaceship)
                if self.game_data.get('spaceship_position'):
                    self.game.spaceship.spaceship_group.sprite.rect.topleft = self.game_data['spaceship_position']

                # Restore mystery ship if active
                #if self.game_data['mystery_active'] and self.game_data.get('mystery_ship_position'):
                #    self.game.mystery_ship.mystery_ship_group.empty()
                #    self.game.mystery_ship.create_mystery_ship()
                #    self.game.mystery_ship.mystery_ship_group.sprite.rect.topleft = self.game_data['mystery_ship_position']
#
                self.game.game_state = True
                return True
                
        except FileNotFoundError:
            return False
        except (KeyError, json.JSONDecodeError) as e:
            print(f"Error loading game: {e}")
            return False
