from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix
#Faz através do cálculo das distâncias mais próximas
#Funciona melhor sem o OneHotEncoder

class Knn:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.knn =None
        self.running_knn()
        self.generate_matrix_confusion()

    def running_knn(self):
        self.knn = KNeighborsClassifier(n_neighbors=30, metric='minkowski', p=2)
        self.knn.fit(self.X_base_time, self.Y_base_time)
        predicts = self.knn.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem do knn de decisão de acerto foi", percentage_predict)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.knn)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)
