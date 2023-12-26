import psycopg2
import config

class Team:
    def __init__(self, id = 0, name = "", code = ""):
        self.db_config = config.db_config
        self.conn_string = "dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'".format(
            **self.db_config)

        self.conn = psycopg2.connect(self.conn_string)
        self.cur = self.conn.cursor()

        self.id = id
        self.name = name
        self.code = code

    def create_team(self, id, name, code):
        query = "INSERT INTO teams (id, name, code) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING"
        self.cur.execute(query, (id, name, code))
        print("Time inserido com sucesso!")

    def get_all_teams(self):
        query = "SELECT * FROM teams"
        self.cur.execute(query)
        listObjects = []
        list = self.cur.fetchall()

        if len(list) > 0:
            for element in list:
                listObjects.append(self.create_team_object(element))
        return listObjects

    def get_team_by_id(self, id):
        query = "SELECT * FROM teams WHERE id = " +str(id)
        self.cur.execute(query)
        element = self.cur.fetchall()
        for e in element:
            return self.create_team_object(e)

    def update_team(self, id, name, code):
        query = "UPDATE teams SET name = %s, code = %s WHERE id = %s"
        self.cur.execute(query, (name, code, id))
        print("Time atualizado com sucesso!")

    def delete_team(self, id):
        query = "DELETE FROM teams WHERE id = %s"
        self.cur.execute(query, (id,))
        print("Time removido com sucesso!")

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def create_team_object(self, result):
        return Team(
            result[0],
            result[1],
            result[2],
        )