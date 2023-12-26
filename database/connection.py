import psycopg2
import config

class ConnectionDatabase:
    def __init__(self):
        self.db_config = config.db_config
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            conn_string = "dbname='{dbname}' user='{user}' password='{password}' host='{host}' port='{port}'".format(
                **self.db_config)
            self.conn = psycopg2.connect(conn_string)
            self.cur = self.conn.cursor()
            print("Conexão estabelecida com sucesso!")
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")

    def desconnect(self):
        if self.conn:
            self.conn.close()
            print("Conexão fechada.")
