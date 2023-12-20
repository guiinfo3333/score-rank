import requests
import psycopg2

import config
from config import db_config


class Request:
    def getStatistics(self, fixture):
        url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/statistics"
        headers = {
            "X-RapidAPI-Key": config.api_key,
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }
        querystring = {"fixture": fixture}

        try:
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
        except requests.RequestException as e:
            print(f"Error during HTTP request: {e}")
            return

        if 'response' not in data:
            print("No response in data")
            return

        try:
            with psycopg2.connect(**db_config) as conn:
                with conn.cursor() as cur:
                    for team_stats in data['response']:
                        team_id = team_stats['team']['id']
                        match_id = querystring['fixture']

                        stats_values = {stat: None for stat in [
                            'shots_on_goal', 'shots_off_goal', 'total_shots', 'blocked_shots',
                            'shots_insidebox', 'shots_outsidebox', 'fouls', 'corner_kicks',
                            'offsides', 'ball_possession', 'yellow_cards', 'red_cards',
                            'goalkeeper_saves', 'total_passes', 'passes_accurate', 'passes_percentage'
                        ]}

                        for stat in team_stats['statistics']:
                            stat_name = stat['type'].lower().replace(' ', '_').replace('%', 'percentage')

                            stats_values[stat_name] = stat['value']

                        columns = ', '.join(stats_values.keys())
                        placeholders = ', '.join(['%s'] * len(stats_values))
                        query = f"INSERT INTO statistics (team_id, match_id, {columns}) VALUES (%s, %s, {placeholders})"
                        values = [team_id, match_id] + list(stats_values.values())

                        # Diagnostic check
                        if len(values) != len(columns.split(',')) + 2:
                            print(
                                f"Mismatch in placeholders and values: {len(columns.split(',')) + 2} vs {len(values)}")
                            continue

                        print("Executing Query...")
                        cur.execute(query, values)

                    conn.commit()
                    print("Data committed to the database.")

        except psycopg2.DatabaseError as e:
            print(f"Database error: {e}")

def obter_times(league_id, start_season, end_season):
        url = "https://api-football-v1.p.rapidapi.com/v3/teams"
        headers = {
            "X-RapidAPI-Key": config.api_key,
            "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
        }

        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        for season in range(start_season, end_season + 1):
            querystring = {"league": league_id, "season": str(season)}
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()

            if 'response' in data:
                teams = data['response']
                for team_info in teams:
                    team_data = team_info.get('team', {})
                    team_id = team_data.get('id')
                    team_name = team_data.get('name')
                    team_code = team_data.get('code')

                    # Inserir somente se o registro não existir na tabela
                    query = "INSERT INTO teams (id, name, code) VALUES (%s, %s, %s) ON CONFLICT (id) DO NOTHING"
                    cur.execute(query, (team_id, team_name, team_code))

        conn.commit()
        cur.close()
        conn.close()




def obter_partida(league_id, start_season, end_season):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures"
    headers = {
        "X-RapidAPI-Key": config.api_key,
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }

    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    for season in range(start_season, end_season + 1):
        querystring = {"league": league_id, "season": str(season)}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()

        if 'response' in data:
            matches = data['response']
            for match_info in matches:
                match_data = match_info.get('fixture', {})
                league_data = match_info.get('league', {})
                team_data = match_info.get('teams', {})
                team_home_data = team_data.get('home', {})
                team_away_data = team_data.get('away', {})
                match_id = match_data.get('id')
                league_season = league_data.get('season')
                league_round = league_data.get('round')
                team_home_id = team_home_data.get('id')
                team_away_id = team_away_data.get('id')

                # Inserir somente se o registro não existir na tabela
                query = "INSERT INTO matches (id, season, round, team_home_id, team_away_id) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING"
                cur.execute(query, (match_id, season, league_round, team_home_id, team_away_id))

    conn.commit()
    cur.close()
    conn.close()
