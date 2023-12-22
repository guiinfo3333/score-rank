from models.matches import Matches


class MatchesController:
    def __init__(self):
        self.matches = Matches()

    def get_by_all_per_team(self, team_home_id, team_away_id):
        return self.matches.get_match_by_id(team_home_id, team_away_id)



