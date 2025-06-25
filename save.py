import json
class Save:

    def __init__(self, game):
        self.__game = game
        self.__mystery_ship_position = None
        self.__spaceship_position = None
        self.__game_data = {}

    # Getters e Setters
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

    # Métodos
    def __inicializar_game_data(self) -> None: # Atribui objetos ao dicionário
        if self.game.spaceship.spaceship_group:
            self.spaceship_position = list(self.game.spaceship.spaceship_group.sprite.rect.topleft)

        # Criar dict game data
        self.game_data = {
            'level': self.game.level,
            'score': self.game.score,
            'highscore': self.game.highscore,
            'lives': self.game.spaceship.player_lives,
            'spaceship_position': self.spaceship_position
        }

    def save_game(self) -> None: # Salva dicionário no json
        self.__inicializar_game_data()
        
        with open('save_game.json', 'w') as file:
            json.dump(self.game_data, file)
        
    def load_game(self) -> bool: # Carrega o estado (vida, posição, etc) guardado no json
        try:
            with open('save_game.json', 'r') as file:
                self.game_data = json.load(file)

                # Carrega esstado do jogo (nível e pontuação)
                self.game.level = self.game_data['level']
                self.game.display.surfaces.level_surface = self.game.display.fonts.font.render(
                    f'LEVEL {self.game.level:02}', False, self.game.display.YELLOW)
                self.game.score = self.game_data['score']
                self.game.highscore = self.game_data['highscore']
                
                # Carrega estado do Jogador
                self.game.spaceship.player_lives = self.game_data['lives']

                # Reinicia as posições
                self.game.mystery_ship.mystery_ship_lasers_group.empty()
                self.game.spaceship.laser_group.empty()
                self.game.alien.aliens_group.empty()
                self.game.alien.aliens_lasers_group.empty()
                self.game.alien.create_aliens(self.game.offset)
                self.game.obstacles = self.game.obstacle.create_obstacles(self.game.screen_height)

                # Restaura posição da Nave do Jogador
                self.game.spaceship.spaceship_group.empty()
                self.game.spaceship.spaceship_group.add(self.game.spaceship)
                if self.game_data.get('spaceship_position'):
                    self.game.spaceship.spaceship_group.sprite.rect.topleft = self.game_data['spaceship_position']

                self.game.game_state = True
                return True
                
        except FileNotFoundError: # Arquivo não encontrado
            return False
        except (KeyError, json.JSONDecodeError) as e: # Chave não encontrada
            print(f"Error loading game: {e}")
            return False
