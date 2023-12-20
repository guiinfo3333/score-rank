import requests
import psycopg2

if __name__ == '__main__':

    # def obter_times(league_id, start_season, end_season):
    #     url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    #     headers = {
    #         "X-RapidAPI-Key": "1480b65befmshf92b3dccec1d75dp169278jsn3f1afd570f1d",
    #         "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    #     }
    #
    #     conn = psycopg2.connect(
    #         dbname="score_rank",
    #         user="postgres",
    #         password="admin",
    #         host="localhost"
    #     )
    #     cur = conn.cursor()
    #
    #     for season in range(start_season, end_season + 1):
    #         querystring = {"league": league_id, "season": str(season)}
    #         response = requests.get(url, headers=headers, params=querystring)
    #         data = response.json()
    #
    #         if 'response' in data:
    #             teams = data['response']
    #             for team_info in teams:
    #                 team_data = team_info.get('team', {})
    #                 team_id = team_data.get('id')
    #                 team_name = team_data.get('name')
    #                 team_code = team_data.get('code')
    #
    #                 # Inserir somente se o registro não existir na tabela
    #                 query = "INSERT INTO teams (id, name, code) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING"
    #                 cur.execute(query, (team_id, team_name, team_code))
    #
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #
    # obter_times("71", 2010, 2022)

    # def obter_partida(league_id, start_season, end_season):
    #     url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    #     headers = {
    #         "X-RapidAPI-Key": "1480b65befmshf92b3dccec1d75dp169278jsn3f1afd570f1d",
    #         "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    #     }
    #
    #     conn = psycopg2.connect(
    #         dbname="score_rank",
    #         user="postgres",
    #         password="admin",
    #         host="localhost"
    #     )
    #     cur = conn.cursor()
    #     for season in range(start_season, end_season + 1):
    #         querystring = {"league": league_id, "season": str(season)}
    #         response = requests.get(url, headers=headers, params=querystring)
    #         data = response.json()
    #
    #         if 'response' in data:
    #             matches = data['response']
    #             for match_info in matches:
    #                 match_data = match_info.get('fixture', {})
    #                 league_data = match_info.get('league', {})
    #                 team_data = match_info.get('teams', {})
    #                 team_home_data = team_data.get('home', {})
    #                 team_away_data = team_data.get('away', {})
    #                 match_id = match_data.get('id')
    #                 league_season = league_data.get('season')
    #                 league_round = league_data.get('round')
    #                 team_home_id = team_home_data.get('id')
    #                 team_away_id = team_away_data.get('id')
    #
    #                 # Inserir somente se o registro não existir na tabela
    #                 query = "INSERT INTO matches (id, season, round, team_home_id, team_away_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING"
    #                 cur.execute(query, (match_id, season, league_round, team_home_id , team_away_id))
    #
    #     conn.commit()
    #     cur.close()
    #     conn.close()
    #
    # obter_partida("71", 2012, 2013)
