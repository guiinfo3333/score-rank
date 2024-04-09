from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

class LogisticRegressionScore:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.log =None
        self.running_logistic_regression()
        self.generate_matrix_confusion()

    def running_logistic_regression(self):
        self.log = LogisticRegression(random_state=1)
        self.log.fit(self.X_base_time, self.Y_base_time)
        predicts = self.log.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem da regressão logística de acerto foi", percentage_predict)


    def predict(self, array):
        return self.log.predict([array])

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.log)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)
