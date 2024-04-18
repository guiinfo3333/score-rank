from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import GridSearchCV
from yellowbrick.classifier import ConfusionMatrix
from v2.classes.generic_algorithm import GenericAlgorithm

class RandomForest(GenericAlgorithm):
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation):
        super().__init__(X_base_time, Y_base_time, X_base_test, Y_base_test, X_base_time_cross_validation, Y_base_time_cross_validation)
        self.running()
        self.cross_validation_with_grid_search()
        self.generate_matrix_confusion()

    def running(self):
        #Posso configurar a quantidade de árvores que vai ser utilizada
        self.forest= RandomForestClassifier(n_estimators=5, criterion='entropy', random_state=0)
        self.forest.fit(self.X_base_time, self.Y_base_time)
        predicts = self.forest.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem florestas randômicas de acerto foi", percentage_predict)

    def cross_validation_with_grid_search(self):
        print("Com cross-validation ==========")
        params = {'criterion': ['gini', 'entropy'],
                      'n_estimators': [10, 40, 100, 150, 5],
                      'min_samples_split': [2, 5, 10],
                      'min_samples_leaf': [1, 5, 10]}

        grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=params)
        grid_search.fit(self.X_base_time_cross_validation, self.Y_base_time_cross_validation)
        melhores_parametros = grid_search.best_params_
        melhor_resultado = grid_search.best_score_
        print(melhores_parametros)
        print(melhor_resultado)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.forest)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)


