from models.predictions import Predictions


class PredictionsController:
    def __init__(self):
        self.results = Predictions()

    def create(self, result_id, predition):
        return self.results.create(result_id, predition)
