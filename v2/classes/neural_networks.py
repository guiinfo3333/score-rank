from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

class NeuralNetwork:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.neural =None
        self.running_neural()
        self.generate_matrix_confusion()

    def running_neural(self):
        self.neural = MLPClassifier(verbose=True, max_iter = 1000, tol=0.000010,
                                  hidden_layer_sizes = (55,55))

        self.neural.fit(self.X_base_time, self.Y_base_time)
        predicts = self.neural.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem rede neural de acerto foi", percentage_predict)

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.neural)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)