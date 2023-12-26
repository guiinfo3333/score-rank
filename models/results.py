import psycopg2
import config
from database.connection import ConnectionDatabase
from utils.constants import CONNECTION


class Results:
    def __init__(self, id = 0, match_id = 0, team_home_id = 0, team_away_id = 0, winner_home = False, winner_away = False, draw = False):
        self.id = id
        self.match_id = match_id
        self.team_home_id = team_home_id
        self.team_away_id = team_away_id
        self.winner_home = winner_home
        self.winner_away = winner_away
        self.draw = draw

    def get_all(self):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM results2023"
        CONNECTION.cur.execute(query)
        list_matches = []

        list = CONNECTION.cur.fetchall()
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_results_object(element))

        CONNECTION.desconnect()
        return list_matches

    def get_results_by_id(self, team_home_id, team_away_id):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM results2023 WHERE (team_home_id = %s and team_away_id = %s)"
        CONNECTION.cur.execute(query, (team_home_id, team_away_id))
        list = CONNECTION.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_results_object(element))
        CONNECTION.desconnect()
        return list_matches


    def create_results_object(self, result):
        return Results(
            result[0],
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
        )