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
        print("numero ae " + str(number))
        if int(number) == int(WINNER):
            return WINNER_HOME
        elif int(number) == int(LOSER):
            return WINNER_AWAY
        else:
            return DRAWER


