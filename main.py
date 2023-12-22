from external.request import Request
from intelligence.intelligence import Intelligence

if __name__ == '__main__':
    request = Request()
    # request.getStatistics("190160")

    # matches_without_stats = request.get_match_id(1)
    # for match_id in matches_without_stats:
    #     request.getStatistics(match_id)

    # request.obter_times(71, 2015,2022)
    # request.obter_partida(71, 2015, 2022)

    print("=========================================== Bem-vindo ao Score Rank =====================================")
    print("======================================= o melhor programa de palpites do mundo =====================================")

    ID_PALMEIRAS = 121
    ID_FLAMENGO = 127

    # A inteligencia sempre analisa se o time que está jogando em CASA vai ganhar, perder ou empatar por aprendizado de máquina
    # Obs = O algoritmo utilizado é o LogisticRegression
    inteligence = Intelligence(matches="Palmeiras x Flamengo", team_home_id=ID_PALMEIRAS, team_way_id= ID_FLAMENGO)
    result_of_game_probability = inteligence.start()

    if result_of_game_probability[0] == 1:
        print(" A probalidade do time da casa empatar nesse jogo é alta. ")
    elif result_of_game_probability[0] == 2:
        print(" A probalidade do time da casa ter uma vitória nesse jogo é alta. ")
    else:
        print(" A probalidade do time da casa perder nesse jogo é alta. ")




