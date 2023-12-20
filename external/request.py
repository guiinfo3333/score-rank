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

                        stats_values = {
                            'shots_on_goal': 0, 'shots_off_goal': 0, 'total_shots': 0, 'blocked_shots': 0,
                            'shots_insidebox': 0, 'shots_outsidebox': 0, 'fouls': 0, 'corner_kicks': 0,
                            'offsides': 0, 'ball_possession': '0%', 'yellow_cards': 0, 'red_cards': 0,
                            'goalkeeper_saves': 0, 'total_passes': 0, 'passes_accurate': 0, 'passes_percentage': '0%'
                        }

                        for stat in team_stats['statistics']:
                            stat_name = stat['type'].lower().replace(' ', '_').replace('%', 'percentage')
                            if stat['value'] is None:
                                stats_values[stat_name] = 0
                            else:
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

    def obter_times(self, league_id, start_season, end_season):
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

    def obter_partida(self, league_id, start_season, end_season):

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
                    goals_data = match_info.get('goals', {})
                    goals_home = goals_data.get('home')
                    goals_away = goals_data.get('away')
                    match_id = match_data.get('id')
                    league_season = league_data.get('season')
                    league_round = league_data.get('round')
                    team_home_id = team_home_data.get('id')
                    team_away_id = team_away_data.get('id')
                    team_home_winner = team_home_data.get('winner')
                    team_away_winner = team_away_data.get('winner')
                    draw = False

                    if team_home_winner == None:
                        team_home_winner = False
                        team_away_winner = False
                        draw = True

                    # Inserir somente se o registro não existir na tabela
                    query_matches = ("INSERT INTO matches (id, season, round, team_home_id, team_away_id,team_home_goals,team_away_goals,winner_home,winner_away, draw) "
                                     "VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s)"
                                     "ON CONFLICT (id) DO NOTHING")
                    cur.execute(query_matches, (match_id, league_season, league_round, team_home_id, team_away_id, goals_home, goals_away,team_home_winner,team_away_winner, draw))

        conn.commit()
        cur.close()
        conn.close()

    def get_match_id(self, limit):
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        query = ("SELECT m.id "
                 "FROM matches m "
                 "LEFT JOIN statistics s ON m.id = s.match_id "
                 "WHERE s.match_id IS NULL "
                 "LIMIT %s")
        cur.execute(query, (limit,))
        match_ids = [match[0] for match in cur.fetchall()]
        cur.close()
        conn.close()
        return match_ids
