import json, os

class Ranking:
    def __init__(self):
        self.ranking_file = 'ranking.json'
        self.scores = []
        self.max_scores = 10
        
        self.load_ranking()

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
            if os.path.exists(self.ranking_file):
                with open(self.ranking_file, 'r') as file:
                    self.scores = json.load(file)
            else:
                self.scores = []
        except:
            self.scores = []
     
    def get_ranking(self) -> list: # Retorna o Ranking
        return self.scores
    