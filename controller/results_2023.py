from models.results import Results


class ResultsController:
    def __init__(self):
        self.results = Results()

    def get_all_results(self):
        return self.results.get_all()

    def get_results_by_id(self, team_home_id, team_away_id):
        return self.results.get_results_by_id(team_home_id, team_away_id)