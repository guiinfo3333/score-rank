import psycopg2

import config

conn = psycopg2.connect(config.db_config)

cur = conn.cursor()

def create_team(id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw):
    query = "INSERT INTO matches (id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING"
    cur.execute(query, (id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw))
    print("Partida inserida com sucesso!")

def get_all_matches():
    query = "SELECT * FROM matches"
    cur.execute(query)
    return cur.fetchall()

def get_match_by_id(id):
    query = "SELECT * FROM matches WHERE id = %s"
    cur.execute(query, (id,))
    return cur.fetchone()

def update_match(id, season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw):
    query = "UPDATE matches SET season = %s, round = %s, team_home_id = %s, team_away_id = %s, team_home_goals = %s, team_away_goals = %s, winner_home = %s, winner_away = %s, draw = %s WHERE id = %s"
    cur.execute(query, (season, round, team_home_id, team_away_id, team_home_goals, team_away_goals, winner_home, winner_away, draw, id))
    print("Partida atualizada com sucesso!")

def delete_match(id):
    query = "DELETE FROM matches WHERE id = %s"
    cur.execute(query, (id,))
    print("Partida removida com sucesso!")
