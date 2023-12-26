from controller.team_controller import TeamController
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


    print("Gerando probabilidades para todos os times que o Fortaleza jogou em casa para o próximo jogo")

    team = TeamController()
    teams_ways = team.get_all()
    ID_TEAM_HOME = 126
    team_home = team.find_by_id(ID_TEAM_HOME)

    for element in teams_ways:
        ID_AWAY = element.id
        if element.id != ID_TEAM_HOME:
            print("Jogo "+ team_home.name + " x " + element.name)
            inteligence = Intelligence(team_home_id=ID_TEAM_HOME, team_way_id=ID_AWAY)
            result_of_game_probability = inteligence.start()

            if result_of_game_probability[0] == 1:
                print(" A probalidade do time da casa empatar nesse jogo é alta. ")
            elif result_of_game_probability[0] == 2:
                print(" A probalidade do time da casa ter uma vitória nesse jogo é alta. ")
            else:
                print(" A probalidade do time da casa perder nesse jogo é alta. ")
            print("=================================================================")








