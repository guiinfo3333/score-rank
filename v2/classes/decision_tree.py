from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from yellowbrick.classifier import ConfusionMatrix

class DecisionTree:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.tree =None
        self.running_decision_tree()
        self.generate_matrix_confusion()
    def running_decision_tree(self):
        self.tree = DecisionTreeClassifier(criterion='entropy')
        self.tree.fit(self.X_base_time, self.Y_base_time)
        predicts = self.tree.predict(self.X_base_test)
        percentage_predict = accuracy_score(self.Y_base_test, predicts)
        print("A porcentagem árvore de decisão de acerto foi", percentage_predict)

    def predict(self, array):
        return self.tree.predict([array])

    def generate_matrix_confusion(self):
        cm = ConfusionMatrix(self.tree)
        cm.fit(self.X_base_time, self.Y_base_time)
        cm.score(self.X_base_test, self.Y_base_test)



