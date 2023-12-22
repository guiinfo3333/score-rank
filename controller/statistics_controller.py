from models.statistics import Statistics


class StatisticsController:
    def __init__(self):
        self.statistic = Statistics()

    def get_by_statistics_per_matche_id(self, matche_id, team_id):
        return self.statistic.get_statistics_per_match_and_time(matche_id, team_id)