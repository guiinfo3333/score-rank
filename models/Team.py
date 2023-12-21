import psycopg2

import config

conn = psycopg2.connect(config.db_config)

cur = conn.cursor()

def create_team(id, name, code):
    query = "INSERT INTO teams (id, name, code) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING"
    cur.execute(query, (id, name, code))
    print("Time inserido com sucesso!")

def get_all_teams():
    query = "SELECT * FROM teams"
    cur.execute(query)
    return cur.fetchall()

def get_team_by_id(id):
    query = "SELECT * FROM teams WHERE id = %s"
    cur.execute(query, (id,))
    return cur.fetchone()

def update_team(id, name, code):
    query = "UPDATE teams SET name = %s, code = %s WHERE id = %s"
    cur.execute(query, (name, code, id))
    print("Time atualizado com sucesso!")

def delete_team(id):
    query = "DELETE FROM teams WHERE id = %s"
    cur.execute(query, (id,))
    print("Time removido com sucesso!")