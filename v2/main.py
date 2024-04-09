import pandas as pd
from v2.classes.data_processing import DataProcessing
from v2.classes.decision_tree import DecisionTree
from v2.classes.knn import Knn
from v2.classes.logistic_regression_score import LogisticRegressionScore
from v2.classes.naves_bayes import NavesBayes
from v2.classes.neural_networks import NeuralNetwork
from v2.classes.random_forest import RandomForest
from v2.classes.svm import Svm

if __name__ == '__main__':
    base_time = pd.read_csv('../csvs/Palmeiras.csv')
    data_processing = DataProcessing(base_time=base_time)

    # naves= NavesBayes(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # decision_tree = DecisionTree(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # random_forest = RandomForest(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # knn = Knn(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # logistic_regression = LogisticRegressionScore(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # svm = Svm(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    svm = NeuralNetwork(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)



