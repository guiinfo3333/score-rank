class GenericAlgorithm:
    def __init__(self, X_base_time, Y_base_time, X_base_test, Y_base_test,  X_base_time_cross_validation, Y_base_time_cross_validation):
        self.X_base_time = X_base_time
        self.Y_base_time = Y_base_time
        self.X_base_test = X_base_test
        self.Y_base_test = Y_base_test
        self.alghoritm = None
        self.X_base_time_cross_validation = X_base_time_cross_validation
        self.Y_base_time_cross_validation = Y_base_time_cross_validation