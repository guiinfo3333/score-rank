from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
from v2.classes.generic_algorithm import GenericAlgorithm

class Svm(GenericAlgorithm):
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation):
        super().__init__(X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation)
        self.running()
        self.cross_validation_with_grid_search()
        self.generate_matrix_confusion()

    def cross_validation_with_grid_search(self):
        print("Com cross-validation ==========")
        parametros = {'tol': [0.001, 0.0001, 0.00001],
                      'C': [1.0, 1.5, 2.0],
                      'kernel': ['rbf', 'linear', 'poly', 'sigmoid']}

        grid_search = GridSearchCV(estimator=SVC(), param_grid=parametros)
        grid_search.fit(self.X_base_time_cross_validation, self.Y_base_time_cross_validation)
        melhores_parametros = grid_search.best_params_
        melhor_resultado = grid_search.best_score_
        print(melhores_parametros)
        print(melhor_resultado)

    def running(self):
        self.alghoritm = SVC(kernel='linear', random_state=1)
        self.alghoritm.fit(self.X_base_time, self.Y_base_time)
        predicts = self.alghoritm.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem svm de acerto foi", percentage_predict)

    def predict(self, array):
        return self.alghoritm.predict([array])

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.alghoritm)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)