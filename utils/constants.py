WINNER_HOME = 'WINNER_HOME'
WINNER_AWAY = 'WINNER_AWAY'
DRAWER = 'DRAW'

DRAW = 1
LOSER = 0
WINNER = 2

CONNECTION = None
class Constants:
    @staticmethod
    def verify_result(object):
        if object.winner_home:
            return WINNER_HOME
        elif object.winner_away:
            return WINNER_HOME
        else:
            return DRAWER

    @staticmethod
    def verify_result_intelligent(number):
        if int(number) == int(WINNER):
            return WINNER_HOME
        elif int(number) == int(LOSER):
            return WINNER_AWAY
        else:
            return DRAWER

    @staticmethod
    def return_list_propertys_times():
        return ['shots_on_goal_home', 'shots_on_goal_away', 'shots_off_goal_home', 'shots_off_goal_away',
                  'total_shots_home', 'total_shots_away', 'blocked_shots_home', 'blocked_shots_away',
                  'shots_insidebox_home', 'shots_insidebox_away', 'fouls_home', 'fouls_away', 'corner_kicks_home',
                  'corner_kicks_away', 'offsides_home', 'offsides_away', 'ball_possession_home', 'ball_possession_away',
                  'yellow_cards_home', 'yellow_cards_away', 'red_cards_home', 'red_cards_away', 'goalkeeper_saves_home',
                  'goalkeeper_saves_away', 'total_passes_home', 'total_passes_away', 'passes_accurate_home',
                  'passes_accurate_away', 'passes_percentage_home', 'passes_percentage_home_away']


