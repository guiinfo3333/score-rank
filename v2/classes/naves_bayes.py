from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Alogritmo Probabilístico
# Este algoritmo se sai melhor sem o oneHotEncoded no tratamento dos dados
class NavesBayes:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.naive_time = None
        self.running_naves_bayes()

    def running_naves_bayes(self):
        self.naive_time = GaussianNB()
        self.naive_time.fit(self.X_base_time, self.Y_base_time)
        predicts = self.naive_time.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem de naves bayer de acerto foi", percentage_predict)

    def predict(self, array):
        return self.naive_time.predict([array])




