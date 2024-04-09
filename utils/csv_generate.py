import csv

class CsvGenerate:
    def __init__(self):
        self.dados = [
            ['home', 'away', 'shots_on_goal_home', 'shots_on_goal_away', 'shots_off_goal_home', 'shots_off_goal_away', 'total_shots_home','total_shots_away','blocked_shots_home', 'blocked_shots_away','shots_insidebox_home','shots_insidebox_away', 'shots_outsidebox_home', 'shots_outsidebox_away', 'fouls_home', 'fouls_away', 'corner_kicks_home', 'corner_kicks_away', 'offsides_home', 'offsides_away', 'ball_possession_home', 'ball_possession_away', 'yellow_cards_home', 'yellow_cards_away', 'red_cards_home', 'red_cards_away', 'goalkeeper_saves_home', 'goalkeeper_saves_away', 'total_passes_home', 'total_passes_away', 'passes_accurate_home', 'passes_accurate_away', 'passes_percentage_home', 'passes_percentage_home_away', 'result']
        ]


    def __len__(self):
        return len(self.dados)

    def add_dados_csv(self, data):
        if data != None:
            self.dados.append(data)

    def generate_csv(self, name):
        nome_arquivo = name+'.csv'

        # Escrevendo os dados no arquivo CSV
        with open(nome_arquivo, 'w', newline='') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            for linha in self.dados:
                escritor_csv.writerow(linha)

        print(f'Arquivo CSV "{nome_arquivo}" gerado com sucesso!')