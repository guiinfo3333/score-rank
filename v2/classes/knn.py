from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from v2.classes.generic_algorithm import GenericAlgorithm

#Faz através do cálculo das distâncias mais próximas
#Funciona melhor sem o OneHotEncoder
class Knn(GenericAlgorithm):
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation):
        super().__init__(X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation)
        self.running()
        self.cross_validation()
        self.generate_matrix_confusion()

    def running(self):
        self.alghoritm = KNeighborsClassifier(n_neighbors=30, metric='minkowski', p=2)
        self.alghoritm.fit(self.X_base_time, self.Y_base_time)
        predicts = self.alghoritm.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem do knn de decisão de acerto foi", percentage_predict)

    #com os cross validation ele testa todos os parametros possiveis, a fim saber quais são os melhores parametros
    def cross_validation(self):
        print("Com cross-validation ==========")
        parametros = {'n_neighbors': [3, 5, 10, 20, 30],
                      'p': [2], 'metric': ['minkowski']}

        grid_search = GridSearchCV(estimator=KNeighborsClassifier(), param_grid=parametros)
        grid_search.fit(self.X_base_time_cross_validation, self.Y_base_time_cross_validation)
        melhores_parametros = grid_search.best_params_
        melhor_resultado = grid_search.best_score_
        print(melhores_parametros)
        print(melhor_resultado)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.alghoritm)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)
