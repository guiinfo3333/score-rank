from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

class Svm:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.svm= None
        self.running_svm()
        self.generate_matrix_confusion()

    def running_svm(self):
        self.svm = SVC(kernel='linear', random_state=1)
        self.svm.fit(self.X_base_time, self.Y_base_time)
        predicts = self.svm.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem svm de acerto foi", percentage_predict)

    def predict(self, array):
        return self.svm.predict([array])

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.svm)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)