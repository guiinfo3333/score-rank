from models.team import Team


class TeamController:
    def __init__(self):
        self.team = Team()

    def get_all(self):
        return self.team.get_all_teams()

    def get_all_personalize(self):
        return self.team.get_all_teams_personalize()

    def find_by_id(self, id):
        return self.team.get_team_by_id(id)