import json

class Ranking:
    def __init__(self):
        self.__ranking_file = 'ranking.json'
        self.__scores = []
        self.__max_scores = 10
        
        self.load_ranking()

    # Getters e Setters
    @property
    def ranking_file(self):
        return self.__ranking_file

    @ranking_file.setter
    def ranking_file(self, value):
        self.__ranking_file = value

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, value):
        self.__scores = value

    @property
    def max_scores(self):
        return self.__max_scores

    @max_scores.setter
    def max_scores(self, value):
        self.__max_scores = value

    # Métodos
    def save_ranking(self) -> None: # Salva as pontuações
        with open(self.ranking_file, 'w') as file:
            json.dump(self.scores, file)
    
    def add_score(self, name, score) -> None: # Adiciona uma nova pontuação, atribuindo-na a um nome de jogador
        score_entry = {'name': name, 'score': score}
        self.scores.append(score_entry)

        self.scores.sort(key = lambda x: x['score'], reverse = True)

        self.scores = self.scores[:self.max_scores]
        self.save_ranking()
 
    def load_ranking(self) -> None: # Carrega o arquivo em self.scores, se este existir
        try:
            with open(self.ranking_file, 'r') as file:
                self.scores = json.load(file)
        except:
            self.scores = []
     
    def get_ranking(self) -> list: # Retorna o Ranking
        return self.scores
    