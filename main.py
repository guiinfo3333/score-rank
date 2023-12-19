import requests
import psycopg2

if __name__ == '__main__':

    def obter_times():
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"
        querystring = {"league": "71", "season": "2011"}
        headers = {
            "X-RapidAPI-Key": "1480b65befmshf92b3dccec1d75dp169278jsn3f1afd570f1d",
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        # Estabelecer conexão com o banco de dados PostgreSQL
        conn = psycopg2.connect(
            dbname="score_rank",
            user="postgres",
            password="postgres",
            host="localhost"
        )
        cur = conn.cursor()

        if 'response' in data:
            teams = data['response']
            for team_info in teams:
                team_data = team_info.get('team', {})
                team_id = team_data.get('id')
                team_name = team_data.get('name')
                team_code = team_data.get('code')

                # Inserir dados no banco de dados
                query = "INSERT INTO teams (team_id, team_name, team_code) VALUES (%s, %s, %s)"
                cur.execute(query, (team_id, team_name, team_code))

        conn.commit()
        cur.close()
        conn.close()

    obter_times()


