from sklearn.model_selection import GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from v2.classes.generic_algorithm import GenericAlgorithm

class NeuralNetwork(GenericAlgorithm):
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation):
        super().__init__(X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation)
        self.running()
        self.cross_validation()
        self.generate_matrix_confusion()

    def cross_validation(self):
        print("Com cross-validation ==========")
        params = {'activation': ['relu', 'logistic', 'tahn'],
                      'solver': ['adam', 'sgd'],
                      'batch_size': [10, 56],
                      'hidden_layer_sizes': [(33,33)],
                      'max_iter': [1000, 200],
                      'tol': [0.000010, 0.0001, 0.001]
                  }

        grid_search = GridSearchCV(estimator=MLPClassifier(), param_grid=params)
        grid_search.fit(self.X_base_time_cross_validation, self.Y_base_time_cross_validation)
        melhores_parametros = grid_search.best_params_
        melhor_resultado = grid_search.best_score_
        print(melhores_parametros)
        print(melhor_resultado)

    #hidden_layer_sizes é calculado a partir da forma (quantidade de atributos +  1) / 2, nesse caso (65 + 1) / 2
    def running(self):
        self.alghoritm = MLPClassifier(verbose=True, max_iter = 1000, tol=0.000010,
                                  hidden_layer_sizes = (33,33))

        self.alghoritm.fit(self.X_base_time, self.Y_base_time)
        predicts = self.alghoritm.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem rede neural de acerto foi", percentage_predict)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.alghoritm)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)