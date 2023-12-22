from models import team


class TeamRepository:
    @staticmethod
    def insert(teamID, name, code):
        new_team = Team(teamID=teamID, name=name, codeTeam=code)
        new_team.save()
        return new_team