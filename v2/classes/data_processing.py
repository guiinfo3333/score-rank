from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from utils.constants import Constants
from sklearn.model_selection import train_test_split
class DataProcessing:
    def __init__(self, base_time):
        self.base_time = base_time
        self.X_base_time = None
        self.Y_base_time = None
        self.X_base_training = None
        self.Y_base_training = None
        self.X_base_test = None
        self.Y_base_test = None
        self.execute_tranform_data()

    def execute_tranform_data(self):
        self.transform_data()
        self.separation_between_predictive_elements_and_classes()
        self.running_label_encoded()
        self.scalling_between_elements()
        self.running_one_hot_encoded()
        self.divide_base_test_in_training()

    def divide_base_test_in_training(self):
        self.X_base_training, self.X_base_test, self.Y_base_training, self.Y_base_test = train_test_split(self.X_base_time, self.Y_base_time, test_size=0.25, random_state=0)
        print("Dados de Treinamento X:" , self.X_base_training.shape)
        print("Dados de Teste X:" , self.X_base_test.shape)

    # devo pegar a média de acordo com o resultado da partida para não ficar zero
    # blocked_shots, red_cars,goalkeeper_saves, total_passes, passes_accurate, passes_percentage - verifcar pq ta vindo zerado em alguns quando tem
    def transform_data(self):
        chaves = Constants.return_list_propertys_times()

        for chave in chaves:
            result = self.base_time[self.base_time[chave] == 0]

            if not result.empty:
                media_derrota = self.base_time[chave][self.base_time["result"] == 0].mean()  # media na derrota
                media_vitoria = self.base_time[chave][self.base_time["result"] == 1].mean()  # media na vitória
                media_empate = self.base_time[chave][self.base_time["result"] == 2].mean()  # media no empate

                self.base_time.loc[(self.base_time[chave] == 0) & (self.base_time["result"] == 0), chave] = media_derrota
                self.base_time.loc[(self.base_time[chave] == 0) & (self.base_time["result"] == 1), chave] = media_vitoria
                self.base_time.loc[(self.base_time[chave] == 0) & (self.base_time["result"] == 2), chave] = media_empate

   #Separa entre elementos previsores e classes
    def separation_between_predictive_elements_and_classes(self):
        self.X_base_time = self.base_time.iloc[:, 0:34].values
        self.Y_base_time = self.base_time.iloc[:, 34].values

    #alguns valores estão maiores que os outros o que pode deixar o algoritmo tendencioso
    def scalling_between_elements(self):
        scaller_base_time = StandardScaler()
        self.X_base_time = scaller_base_time.fit_transform(self.X_base_time)

    # Transforma variaveis nominais em variaveis matematicas
    def running_label_encoded(self):
        label_encoder_team_home = LabelEncoder()
        label_encoder_team_away = LabelEncoder()
        self.X_base_time[:, 0] = label_encoder_team_home.fit_transform(self.X_base_time[:, 0])
        self.X_base_time[:, 1] = label_encoder_team_away.fit_transform(self.X_base_time[:, 1])

    # Mesmo aplicando o label encoded pode ser que tenha muitos valores de 1 a 100 por exemplo, assim é preciso fazer um one hot encoded
    def running_one_hot_encoded(self):
        # numero = len(np.unique(base_time['away']))
        onehotencoder_base_time = ColumnTransformer(transformers=[('OneHot', OneHotEncoder(), [1])], remainder='passthrough')
        self.X_base_time = onehotencoder_base_time.fit_transform(self.X_base_time)
