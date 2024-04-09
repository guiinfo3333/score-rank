from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

class RandomForest():
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.forest = None
        self.running_random_forest()
        self.generate_matrix_confusion()

    def running_random_forest(self):
        #Posso configurar a quantidade de árvores que vai ser utilizada
        self.forest= RandomForestClassifier(n_estimators=5, criterion='entropy', random_state=0)
        self.forest.fit(self.X_base_time, self.Y_base_time)
        predicts = self.forest.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem florestas randômicas de acerto foi", percentage_predict)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.forest)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)


