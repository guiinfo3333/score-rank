import psycopg2
import config

class Results:
    def __init__(self, id = 0, match_id = 0, team_home_id = 0, team_away_id = 0, winner_home = False, winner_away = False, draw = False):
        self.db_config = config.db_config
        self.conn_string = "dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'".format(
            **self.db_config)

        self.conn = psycopg2.connect(self.conn_string)
        self.cur = self.conn.cursor()

        self.id = id
        self.match_id = match_id
        self.team_home_id = team_home_id
        self.team_away_id = team_away_id
        self.winner_home = winner_home
        self.winner_away = winner_away
        self.draw = draw

    def get_all(self):
        query = "SELECT * FROM results2023"
        self.cur.execute(query)
        return self.cur.fetchall()

    def get_results_by_id(self, team_home_id, team_away_id):
        query = "SELECT * FROM results2023 WHERE (team_home_id = %s and team_away_id = %s)"
        self.cur.execute(query, (team_home_id, team_away_id))
        list = self.cur.fetchall()
        list_matches = []
        if len(list) > 0:
            for element in list:
                list_matches.append(self.create_matches_object(element))

        return list_matches

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def create_results_object(self, result):
        return Results(
            result[0],
            result[1],
            result[2],
        )