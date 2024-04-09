import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# devo pegar a média de acordo com o resultado da partida para não ficar zero
# blocked_shots, red_cars,goalkeeper_saves, total_passes, passes_accurate, passes_percentage - verifcar pq ta vindo zerado em alguns quando tem
def tratamento_dados(base_time):
    print(base_time)
    chaves = ['shots_on_goal_home', 'shots_on_goal_away', 'shots_off_goal_home', 'shots_off_goal_away', 'total_shots_home', 'total_shots_away', 'blocked_shots_home', 'blocked_shots_away', 'shots_insidebox_home', 'shots_insidebox_away', 'fouls_home', 'fouls_away', 'corner_kicks_home', 'corner_kicks_away', 'offsides_home', 'offsides_away', 'ball_possession_home', 'ball_possession_away', 'yellow_cards_home', 'yellow_cards_away', 'red_cards_home', 'red_cards_away', 'goalkeeper_saves_home', 'goalkeeper_saves_away', 'total_passes_home', 'total_passes_away', 'passes_accurate_home', 'passes_accurate_away', 'passes_percentage_home', 'passes_percentage_home_away']

    for chave in chaves:
        result = base_time[base_time[chave] == 0]

        if not result.empty:
            media_derrota = base_time[chave][base_time["result"] == 0].mean() #media na derrota
            media_vitoria = base_time[chave][base_time["result"] == 1].mean() #media na vitória
            media_empate = base_time[chave][base_time["result"] == 2].mean()  #media no empate

            base_time.loc[(base_time[chave] == 0) & (base_time["result"] == 0), chave] = media_derrota
            base_time.loc[(base_time[chave] == 0) & (base_time["result"] == 1), chave] = media_vitoria
            base_time.loc[(base_time[chave] == 0) & (base_time["result"] == 2), chave] = media_empate

    return base_time

def separamento_entre_elementos_previsores_e_classe(base_time):
    X_base_time = base_time.iloc[:, 0:34].values
    Y_base_time = base_time.iloc[:, 34].values
    return X_base_time, Y_base_time


#alguns valores estão maiores que os outros o que pode deixar o algoritmo tendencioso
def escalonamento_entre_os_elementos(X_base_time):
    scaller_base_time = StandardScaler()
    X_base_time = scaller_base_time.fit_transform(X_base_time)
    return X_base_time


# Transforma variaveis nominais em variaveis matematicas
def executando_label_encoded(X_base_time):
    label_encoder_team_home = LabelEncoder()
    label_encoder_team_away = LabelEncoder()
    X_base_time[:, 0] = label_encoder_team_home.fit_transform(X_base_time[:, 0])
    X_base_time[:, 1] = label_encoder_team_away.fit_transform(X_base_time[:, 1])
    return X_base_time

# Mesmo aplicando o label encoded pode ser que tenha muitos valores de 1 a 100 por exemplo, assim é preciso fazer um one hot encoded
def executando_one_hot_encoded(X_base_time):
    # numero = len(np.unique(base_time['away']))
    onehotencoder_base_time = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
    X_base_time = onehotencoder_base_time.fit_transform(X_base_time)
    return X_base_time



if __name__ == '__main__':
    base_time = pd.read_csv('../csvs/Palmeiras.csv')
    base_time = tratamento_dados(base_time)
    X_base_time, Y_base_time = separamento_entre_elementos_previsores_e_classe(base_time)
    X_base_time = executando_label_encoded(X_base_time)
    X_base_time = escalonamento_entre_os_elementos(X_base_time)
    X_base_time = executando_one_hot_encoded(X_base_time)
    print(base_time)
    print("alo")


