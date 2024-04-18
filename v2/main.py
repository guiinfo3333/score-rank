import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from v2.classes.data_processing import DataProcessing
from v2.classes.decision_tree import DecisionTree
from v2.classes.knn import Knn
from v2.classes.logistic_regression_score import LogisticRegressionScore
from v2.classes.naves_bayes import NavesBayes
from v2.classes.neural_networks import NeuralNetwork
from v2.classes.random_forest import RandomForest
from v2.classes.svm import Svm
from scipy.stats import shapiro
from scipy.stats import f_oneway
from statsmodels.stats.multicomp import MultiComparison

if __name__ == '__main__':
    base_time = pd.read_csv('../csvs/Palmeiras.csv')
    data_processing = DataProcessing(base_time=base_time)

    # naves= NavesBayes(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test)
    # decision_tree = DecisionTree(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)
    # random_forest = RandomForest(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)
    # knn = Knn(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)
    # logistic_regression = LogisticRegressionScore(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)
    # svm = Svm(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)
    # svm = NeuralNetwork(data_processing.X_base_training, data_processing.Y_base_training, data_processing.X_base_test, data_processing.Y_base_test, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation)



    # Aplicando  a validacao cruzada, depois de ter verificado os melhores parametros
    #ele vai  dividir os dados em 10 grupos, sempre pegando 9 para teste e 1 para treino, depois gera a média de cada uma delas
    resultados_arvore = []
    resultados_random_forest = []
    resultados_knn = []
    resultados_logistica = []
    resultados_svm = []
    resultados_rede_neural = []

    for i in range(30):
        print(i)
        kfold = KFold(n_splits=10, shuffle=True, random_state=i)

        arvore = DecisionTreeClassifier(criterion='gini', min_samples_leaf=10, min_samples_split=2, splitter='best')
        scores = cross_val_score(arvore, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        # print(scores)
        # print(scores.mean())
        resultados_arvore.append(scores.mean())

        random_forest = RandomForestClassifier(criterion='entropy', min_samples_leaf=1, min_samples_split=5,
                                               n_estimators=150)
        scores = cross_val_score(random_forest, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        resultados_random_forest.append(scores.mean())
        #
        # knn = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
        # scores = cross_val_score(knn, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        # resultados_knn.append(scores.mean())
        #
        # logistica = LogisticRegression(C=1.0, solver='lbfgs', tol=0.00001)
        # scores = cross_val_score(logistica, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        # resultados_logistica.append(scores.mean())
        #
        # svm = SVC(kernel='linear', C=1.0)
        # scores = cross_val_score(svm, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        # resultados_svm.append(scores.mean())
        #
        # rede_neural = MLPClassifier(activation='logistic', batch_size=10, solver='adam', hidden_layer_sizes=(33,33), max_iter=1000, tol=0.00001)
        # scores = cross_val_score(rede_neural, data_processing.X_base_time_cross_validation, data_processing.Y_base_time_cross_validation, cv=kfold)
        # resultados_rede_neural.append(scores.mean())

    resultados = pd.DataFrame({'Arvore': resultados_arvore, 'Random forest': resultados_random_forest})
                               # 'KNN': resultados_knn, 'Logistica': resultados_logistica,
                               # 'SVM': resultados_svm, 'Rede neural': resultados_rede_neural})
    print(resultados)

    #o std representa  o desvio padrão que é o quando os valores estão afastados da média
    print("printa a tabela")
    print(resultados.describe())

    print("Variância ===")
    # mostra a varianca dos resultados
    print(resultados.var())

    print("Coeficiente de Variacão ===")
    print((resultados.std() / resultados.mean()) * 100)


    #Avaliacção de Algoritmos de Classificação
    #alpha é a probabilidade de rejeitar  a hipotese nula que  é de 5%
    alpha = 0.05

    # a lib shapior testa as hipoteses verificando se cada uma das alternativas está na distribuicao normal,
    #se o segundo parametro for menor que 0.05 quer dizer que não segue uma distribuição normal
    print(shapiro(resultados_arvore), shapiro(resultados_random_forest), shapiro(resultados_knn), shapiro(
        resultados_logistica), shapiro(resultados_svm), shapiro(resultados_rede_neural))



    #Teste de Hipotese com Anova e Turkey, servem para comparar estatisticamente se um algoritmo é melhor que  o outro
    _, p = f_oneway(resultados_arvore, resultados_random_forest, resultados_knn, resultados_logistica, resultados_svm,
                    resultados_rede_neural)

    alpha = 0.05
    if p <= alpha:
        print('Hipótese nula rejeitada. Dados são diferentes')
    else:
        print('Hipótese alternativa rejeitada. Resultados são iguais')

    resultados_algoritmos = {'accuracy': np.concatenate(
        [resultados_arvore, resultados_random_forest, resultados_knn, resultados_logistica, resultados_svm,
         resultados_rede_neural]),
                             'algoritmo': ['arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore',
                                           'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore',
                                           'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore',
                                           'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore', 'arvore',
                                           'arvore', 'arvore',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest', 'random_forest', 'random_forest',
                                           'random_forest', 'random_forest',
                                           'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn',
                                           'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn',
                                           'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn', 'knn',
                                           'logistica', 'logistica', 'logistica', 'logistica', 'logistica', 'logistica',
                                           'logistica', 'logistica', 'logistica', 'logistica', 'logistica', 'logistica',
                                           'logistica', 'logistica', 'logistica', 'logistica', 'logistica', 'logistica',
                                           'logistica', 'logistica', 'logistica', 'logistica', 'logistica', 'logistica',
                                           'logistica', 'logistica', 'logistica', 'logistica', 'logistica', 'logistica',
                                           'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm',
                                           'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm',
                                           'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm', 'svm',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural',
                                           'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural', 'rede_neural']}
    resultados_df = pd.DataFrame(resultados_algoritmos)
    print(resultados_df)

    compara_algoritmos = MultiComparison(resultados_df['accuracy'], resultados_df['algoritmo'])
    teste_estatistico = compara_algoritmos.tukeyhsd()
    print(teste_estatistico)
    print(resultados.mean())
    print(teste_estatistico.plot_simultaneous())

