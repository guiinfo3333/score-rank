import psycopg2

import config

conn = psycopg2.connect(config.db_config)

cur = conn.cursor()

def create_statistics(team_id, match_id, shots_on_goal, shots_off_goal,total_shots, blocked_shots, shots_insidebox,
                      shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, yellow_cards, red_cards,
                      goalkeeper_saves, total_passes, passes_accurate, passes_percentage):
    query = ("INSERT INTO statistics (team_id, match_id, shots_on_goal, shots_off_goal, total_shots, "
             "blocked_shots, shots_insidebox, shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, "
             "yellow_cards, red_cards, goalkeeper_saves, total_passes, passes_accura, passes_percen ) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s) "
             "ON CONFLICT (team_id) DO NOTHING")
    cur.execute(query, (team_id, match_id, shots_on_goal, shots_off_goal,total_shots, blocked_shots, shots_insidebox,
                      shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, yellow_cards, red_cards,
                      goalkeeper_saves, total_passes, passes_accurate, passes_percentage))
    print("Estatistica inserida com sucesso!")

def get_all_statistics():
    query = "SELECT * FROM statistics"
    cur.execute(query)
    return cur.fetchall()

def get_statistics_by_id(id):
    query = "SELECT * FROM statistics WHERE id = %s"
    cur.execute(query, (id,))
    return cur.fetchone()

def update_statistics(id, team_id, match_id, shots_on_goal, shots_off_goal,total_shots, blocked_shots, shots_insidebox,
                      shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, yellow_cards, red_cards,
                      goalkeeper_saves, total_passes, passes_accurate, passes_percentage):
    query = ("UPDATE statistics SET team_id = %s, match_id = %s, shots_on_goal = %s, shots_off_goal = %s, "
             "total_shots = %s, blocked_shots = %s, shots_insidebox = %s, shots_outsidebox = %s, fouls = %s, "
             "corner_kicks = %s, offsides = %s, ball_possession = %s, yellow_cards = %s, red_cards = %s, "
             "goalkeeper_saves = %s, total_passes = %s, passes_accurate = %s, passes_percentage = %s WHERE id = %s")
    cur.execute(query, (team_id, match_id, shots_on_goal, shots_off_goal,total_shots, blocked_shots, shots_insidebox,
                      shots_outsidebox, fouls, corner_kicks, offsides, ball_possession, yellow_cards, red_cards,
                      goalkeeper_saves, total_passes, passes_accurate, passes_percentage, id))
    print("Estatistica atualizada com sucesso!")

def delete_statistics(id):
    query = "DELETE FROM statistics WHERE id = %s"
    cur.execute(query, (id,))
    print("Estatistica removida com sucesso!")