from models.team import Team


class TeamController:
    def __init__(self):
        self.team = Team()

    def get_all(self):
        return self.team.get_all_teams()