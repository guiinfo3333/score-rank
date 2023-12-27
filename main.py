from intelligence.intelligence import Intelligence
from controller.team_controller import TeamController
from utils.utils import Utils

if __name__ == '__main__':
    print("=========================================== Bem-vindo ao Score Rank =====================================")
    print("======================================= o melhor programa de palpites do mundo =====================================")
    Utils.print_mad()

    while True:
        print("Operações: \n0.Sair \n1.Listar times \n2.Gerar resultados \n3.Percentuais ")
        choice = input("Escolha uma opção (0/1/2/3): ")

        if choice == '0':
            break

        if choice == '1':
            team = TeamController()
            teams_ways = team.get_all()
            for element in teams_ways:
             print("Resultado:", "ID:",element.id, "Nome:", element.name)
        elif choice == '2':
            team = TeamController()
            teams_ways = team.get_all()
            ID_TEAM_HOME = input('Insira o ID do time da casa:')
            team_home = team.find_by_id(ID_TEAM_HOME)

            for element in teams_ways:
                ID_AWAY = element.id
                if element.id != ID_TEAM_HOME:
                    print("Jogo " + team_home.name + " x " + element.name)
                    inteligence = Intelligence(team_home_id=ID_TEAM_HOME, team_way_id=ID_AWAY)
                    result_of_game_probability = inteligence.start()

                    if result_of_game_probability[0] == 1:
                        print(" A probalidade do time da casa empatar nesse jogo é alta. ")
                    elif result_of_game_probability[0] == 2:
                        print(" A probalidade do time da casa ter uma vitória nesse jogo é alta. ")
                    else:
                        print(" A probalidade do time da casa perder nesse jogo é alta. ")
                    print("=================================================================")
        elif choice == '3':
            inteligence = Intelligence()
            inteligence.percentage_machine_2023()
        else:
            print("Opção inválida!")





