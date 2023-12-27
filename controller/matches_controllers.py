from models.matches import Matches


class MatchesController:
    def __init__(self):
        self.matches = Matches()

    def get_by_all_per_team(self, team_home_id, team_away_id):
        return self.matches.get_match_by_id(team_home_id, team_away_id)


    # Pega os últimos tres jogos em casa, os 3 ultimos fora, e os ultimos tres entre eles
    def get_by_all_per_team_personalize(self, team_home_id, team_away_id):
        list_last_three_in_away = self.matches.get_match_by_last_three_away_games(team_home_id)
        list_last_three_in_home = self.matches.get_match_by_last_three_home_games(team_home_id)
        list_last_three_between = self.matches.get_match_by_last_three_games_between(team_home_id, team_away_id)

        return list_last_three_in_away + list_last_three_in_home + list_last_three_between



