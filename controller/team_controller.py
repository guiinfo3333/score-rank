import requests


def obter_times():
    url = "https://api-football-v1.p.rapidapi.com/v3/teams"
    querystring = {"league": "71", "season": "2010"}
    headers = {
        "X-RapidAPI-Key": "1480b65befmshf92b3dccec1d75dp169278jsn3f1afd570f1d",
        "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    if 'response' in data:
        teams = data['response']
        for team_infor in teams:
            team_data = team_infor.get('team', [])
            team_id = team_data.get('id')
            team_name = team_data.get('name')
            team_code = team_data.get('code')
            print(team_id, team_name, team_code)