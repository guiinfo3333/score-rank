from controller.predictions import PredictionsController
from external.request import Request
from intelligence.intelligence import Intelligence
from models.results import Results
from utils.constants import Constants

if __name__ == '__main__':
    request = Request()
    # request.getStatistics("190160")

    # matches_without_stats = request.get_match_id(1)
    # for match_id in matches_without_stats:
    #     request.getStatistics(match_id)

    # request.obter_times(71, 2015,2022)
    # request.obter_partida(71, 2015, 2022)
    # request.get_results_2023(2023)

    print("=========================================== Bem-vindo ao Score Rank =====================================")
    print("======================================= o melhor programa de palpites do mundo =====================================")


    # print("Gerando probabilidades para todos os times que o Fortaleza jogou em casa para o próximo jogo")
    #
    # team = TeamController()
    # teams_ways = team.get_all()
    # ID_TEAM_HOME = 126
    # team_home = team.find_by_id(ID_TEAM_HOME)
    #
    # for element in teams_ways:
    #     ID_AWAY = element.id
    #     if element.id != ID_TEAM_HOME:
    #         print("Jogo "+ team_home.name + " x " + element.name)
    #         inteligence = Intelligence(team_home_id=ID_TEAM_HOME, team_way_id=ID_AWAY)
    #         result_of_game_probability = inteligence.start()
    #
    #         if result_of_game_probability[0] == 1:
    #             print(" A probalidade do time da casa empatar nesse jogo é alta. ")
    #         elif result_of_game_probability[0] == 2:
    #             print(" A probalidade do time da casa ter uma vitória nesse jogo é alta. ")
    #         else:
    #             print(" A probalidade do time da casa perder nesse jogo é alta. ")
    #         print("=================================================================")
    #


    # Testando se a máquina é boa mesmo
    results2023 = Results()
    list = results2023.get_all()

    for l in list:
        if isinstance(l, Results):
            print(l.team_home_id, l.team_away_id)
            result_real = Constants.verify_result(l)
            inteligence = Intelligence(team_home_id=l.team_home_id, team_way_id= l.team_away_id)
            result_of_game_probability = inteligence.start()

            if result_of_game_probability != "Não há dados de partidas entre estes dois times":
                result_intelligence = Constants.verify_result_intelligent(result_of_game_probability[0])

                correct_result = False
                if result_real == result_intelligence:
                    correct_result = True

                prediction = PredictionsController().create(l.id, correct_result)








