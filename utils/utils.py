from models.statistics import Statistics


class Utils:
    def mounted_data_machine_learning(self, statistics_home, statistics_away):
       if (isinstance(statistics_home, Statistics) and isinstance(statistics_away, Statistics)):
            data = [
                statistics_home.shots_on_goal,
                statistics_away.shots_on_goal,
                statistics_home.shots_off_goal,
                statistics_away.shots_off_goal,
                statistics_home.total_shots,
                statistics_away.total_shots,
                statistics_home.blocked_shots,
                statistics_away.blocked_shots,
                statistics_home.shots_insidebox,
                statistics_away.shots_insidebox,
                statistics_home.shots_outsidebox,
                statistics_away.shots_outsidebox,
                statistics_home.fouls,
                statistics_away.fouls,
                statistics_home.corner_kicks,
                statistics_away.corner_kicks,
                statistics_home.offsides,
                statistics_away.offsides,
                statistics_home.ball_possession.replace("%", ""),
                statistics_away.ball_possession.replace("%", ""),
                statistics_home.yellow_cards,
                statistics_away.yellow_cards,
                statistics_home.red_cards,
                statistics_away.red_cards,
                statistics_home.goalkeeper_saves,
                statistics_away.goalkeeper_saves,
                statistics_home.total_passes,
                statistics_away.total_passes,
                statistics_home.passes_accurate,
                statistics_away.passes_accurate,
                statistics_home.passes_percentage.replace("%",""),
                statistics_away.passes_percentage.replace("%",""),
            ]

            data_convertida = []
            for item in data:
                item = float(item)
                data_convertida.append(item)

            return data_convertida

       raise TypeError("O argumento deve do tipo Statistics.")

    def verify_unic_array(self, list):
        result = True
        number = 0

        if len(list) > 0:
            number = list[0]
            for element in list:
                if element != number:
                    return False

        return True

    @staticmethod
    def print_mad():
       print("                ##########   ")
       print("            ####################")
       print("         ######    ########    #### ")
       print("       ####          ##            ## ")
       print("       ##                            ## ")
       print("     ####                          ###### ")
       print("     ######          ####          ######   ")
       print("   ########        ########        ######     ")
       print("   ######      ##############      ######      ")
       print("   ####        ##############          ####    ")
       print("   ##            ############          ####    ")
       print("   ##            ############          ##      ")
       print("     ##          ##########            ##      ")
       print("     ##                                ##      ")
       print("     ####                            ##        ")
       print("       ########              ##########        ")
       print("         ########            ########          ")
       print("           ######            ######            ")
       print("             ##################                ")
       print("                     ####                      ")

