from database.connection import ConnectionDatabase


class Predictions:
    def __init__(self, id = 0, result_id = 0, prediction = False):
        self.id = id
        self.result_id = result_id
        self.prediction = prediction

    def create(self, results_id, predition):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()

        query = "INSERT INTO predictions (results_id, predition) VALUES (%s, %s) ON CONFLICT (id) DO NOTHING"
        CONNECTION.cur.execute(query, (results_id, predition))
        CONNECTION.conn.commit()
        CONNECTION.desconnect()
