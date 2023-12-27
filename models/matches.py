import psycopg2
import config
from database.connection import ConnectionDatabase


class Matches:
    def __init__(self, id = 0, season = 0, round = "", team_home_id = 0, team_away_id = 0, team_home_goals = 0, team_away_goals = 0, winner_home = False, winner_away = False, draw = False):
        self.id = id
        self.season = season
        self.round = round
        self.team_home_id = team_home_id
        self.team_away_id = team_away_id
        self.team_home_goals = team_home_goals
        self.team_away_goals = team_away_goals
        self.winner_home = winner_home
        self.winner_away = winner_away
        self.draw = draw

    def create_team(self, id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw):
        CONNECTION = ConnectionDatabase()
        query = "INSERT INTO matches (id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING"
        CONNECTION.cur.execute(query, (id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw))
        CONNECTION.desconnect()
        print("Partida inserida com sucesso!")

    def get_all_matches(self):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches"
        self.cur.execute(query)
        list = self.cur.fetchall()
        CONNECTION.desconnect()
        return list

    def get_all_matches_per_temas(self):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches"
        CONNECTION.cur.execute(query)
        list = self.cur.fetchall()
        CONNECTION.desconnect()
        return list

    def get_match_last_five(self, team_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches WHERE team_home_id = %s or team_away_id = %s order by season, round DESC limit 5"
        CONNECTION.cur.execute(query, (team_id, team_id))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))

        CONNECTION.desconnect()
        return list_matches

    def get_match_by_id(self, team_home_id, team_away_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches WHERE (team_home_id = %s and team_away_id = %s) order by season, round"
        CONNECTION.cur.execute(query, (team_home_id, team_away_id))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))

        CONNECTION.desconnect()
        return list_matches

    def get_match_by_last_three_games_between(self, team_home_id, team_away_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = f"SELECT * FROM matches WHERE (team_home_id = %s and team_away_id = %s) or (team_home_id = %s and team_away_id = %s) order by season DESC limit 3"
        CONNECTION.cur.execute(query, (team_home_id, team_away_id, team_away_id, team_home_id))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))

        CONNECTION.desconnect()
        return list_matches

    def get_match_by_last_three_home_games(self, team_home_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches WHERE team_home_id = %s order by season DESC limit 3"
        CONNECTION.cur.execute(query, (team_home_id, ))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))

        CONNECTION.desconnect()
        return list_matches

    def get_match_by_last_three_away_games(self, team_away_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM matches WHERE team_away_id = %s order by season DESC limit 3"
        CONNECTION.cur.execute(query, (team_away_id, ))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))
        CONNECTION.desconnect()

        return list_matches

    def update_match(self, id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw):
        query = "UPDATE matches SET season = %s, round = %s, team_home_id = %s, team_away_id = %s, team_home_goals = %s, team_away_goals = %s, winner_home = %s, winner_away = %s, draw = %s WHERE id = %s"
        self.cur.execute(query, (season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw, id))
        print("Partida atualizada com sucesso!")

    def delete_match(self, id):
        query = "DELETE FROM matches WHERE id = %s"
        self.cur.execute(query, (id,))
        print("Partida removida com sucesso!")


    def create_matches_object(self, result):
        return Matches(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7],
            result[8],
            result[9],
        )