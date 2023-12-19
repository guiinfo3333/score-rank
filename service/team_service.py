from repository import team_repository


class TeamService:
    @staticmethod
    def insert_payload(teamID,name,code):
        return team_repository.TeamRepository.insert(teamID,name,code)