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

    def get_percentage(self):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT (COUNT(CASE WHEN predition = TRUE THEN 1 END)::FLOAT / COUNT(*)) * 100 as percentual_acerto, (COUNT(CASE WHEN predition = FALSE THEN 1 END)::FLOAT / COUNT(*)) * 100 as percentual_erro FROM predictions;"
        CONNECTION.cur.execute(query)
        list = CONNECTION.cur.fetchall()
        return list

    def get_prediction(self):
        CONNECTION = ConnectionDatabase()
        CONNECTION.connect()
        query = "SELECT * FROM predictions;"
        CONNECTION.cur.execute(query)
        list = CONNECTION.cur.fetchall()
        return list