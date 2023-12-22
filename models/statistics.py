import psycopg2
import config

class Statistics:
    def __init__(self, id = 0, team_id = 0, match_id = 0, shots_on_goal = 0, shots_off_goal = 0, total_shots = 0,
            blocked_shots = 0, shots_insidebox = 0, shots_outsidebox = 0, fouls = 0,
            corner_kicks = 0, offsides = 0, ball_possession = "",
            yellow_cards = 0, red_cards = 0, goalkeeper_saves = 0,
            total_passes = 0, passes_accurate = 0, passes_percentage = ""):

        self.db_config = config.db_config
        self.conn_string = "dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'".format(
            **self.db_config)

        self.conn = psycopg2.connect(self.conn_string)
        self.cur = self.conn.cursor()

        self.id = id
        self.team_id = team_id
        self.match_id = match_id
        self.shots_on_goal = shots_on_goal
        self.shots_off_goal = shots_off_goal
        self.total_shots = total_shots
        self.blocked_shots = blocked_shots
        self.shots_insidebox = shots_insidebox
        self.shots_outsidebox = shots_outsidebox
        self.fouls = fouls
        self.corner_kicks = corner_kicks
        self.offsides = offsides
        self.ball_possession = ball_possession
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards
        self.goalkeeper_saves = goalkeeper_saves
        self.total_passes = total_passes
        self.passes_accurate = passes_accurate
        self.passes_percentage = passes_percentage

    def create_statistics(self, team_id, match_id, shots_on_goal, shots_off_goal, total_shots, blocked_shots,
                          shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession,
                          yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accurate, passes_percentage):
        query = ("INSERT INTO statistics (team_id, match_id, shots_on_goal, shots_off_goal, total_shots, "
                 "blocked_shots, shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, "
                 "yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accura, passes_percen ) "
                 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s) "
                 "ON CONFLICT (team_id) DO NOTHING")
        self.cur.execute(query, (team_id, match_id, shots_on_goal, shots_off_goal, total_shots, blocked_shots,
                                 shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession,
                                 yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accurate,
                                 passes_percentage))
        print("Estatística inserida com sucesso!")

    def get_all_statistics(self):
        query = "SELECT * FROM statistics"
        self.cur.execute(query)
        list = self.cur.fetchall()

        list_statistics = []
        if len(list) > 0:
            for element in list:
                list_statistics.append(self.create_statistic_object(element))

        return list_statistics

    def get_statistics_by_id(self, id):
        query = "SELECT * FROM statistics WHERE id = %s"
        self.cur.execute(query, (id,))
        return self.cur.fetchone()

    def get_statistics_per_match_and_time(self, match_id, team_id):
        query = "SELECT * FROM statistics WHERE match_id = %s and team_id = %s"
        self.cur.execute(query, (match_id, team_id))
        element = self.cur.fetchone()
        return self.create_statistic_object(element)

    def update_statistics(self, id, team_id, match_id, shots_on_goal, shots_off_goal, total_shots, blocked_shots,
                          shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession,
                          yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accurate, passes_percentage):
        query = ("UPDATE statistics SET team_id = %s, match_id = %s, shots_on_goal = %s, shots_off_goal = %s, "
                 "total_shots = %s, blocked_shots = %s, shots_insidebox = %s, shots_outsidebox = %s, fouls = %s, "
                 "corner_kicks = %s, offsides = %s, ball_possession = %s, yellow_cards = %s, red_cards = %s, "
                 "goalkeeper_saves = %s, total_passes = %s, passes_accurate = %s, passes_percentage = %s WHERE id = %s")
        self.cur.execute(query, (team_id, match_id, shots_on_goal, shots_off_goal, total_shots, blocked_shots,
                                 shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession,
                                 yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accurate,
                                 passes_percentage, id))
        print("Estatística atualizada com sucesso!")

    def delete_statistics(self, id):
        query = "DELETE FROM statistics WHERE id = %s"
        self.cur.execute(query, (id,))
        print("Estatística removida com sucesso!")

    def __del__(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def transformInLineDataSet(self):
        return [self.shots_on_goal, self.shots_off_goal, self.total_shots,
                          self.blocked_shots, self.shots_insidebox, self.fouls,
                          self.corner_kicks, self.offsides, self.ball_possession,
                          self.yellow_cards, self.red_cards, self.goalkeeper_saves,
                          self.total_passes, self.passes_accurate, self.passes_percentage]

    def create_statistic_object(self, result):
        return Statistics(
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
            result[10],
            result[11],
            result[12],
            result[13],
            result[14],
            result[15],
            result[16],
            result[17],
            result[18],
        )