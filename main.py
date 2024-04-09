from intelligence.intelligence import Intelligence
from controller.team_controller import TeamController
from utils.csv_generate import CsvGenerate
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
            # ID_TEAM_HOME = input('Insira o ID do time da casa:')
            team_home = team.get_all_personalize()

            for element1 in team_home:
                csv = CsvGenerate()

                for element in teams_ways:
                    ID_AWAY = element.id
                    if element.id != element1.id:
                        print("Jogo " + element1.name + " x " + element.name)
                        inteligence = Intelligence(team_home_id=element1.id, team_way_id=ID_AWAY, csv = csv, name_team_home=element1.name, name_team_away= element.name)
                        result_of_game_probability = inteligence.start()

                        if result_of_game_probability[0] == 1:
                            print(" A probalidade do time da casa empatar nesse jogo é alta. ")
                        elif result_of_game_probability[0] == 2:
                            print(" A probalidade do time da casa ter uma vitória nesse jogo é alta. ")
                        else:
                            print(" A probalidade do time da casa perder nesse jogo é alta. ")
                        print("=================================================================")
                        csv.generate_csv(element1.name)
        elif choice == '3':
            inteligence = Intelligence()
            inteligence.spercentage_machine_2023()
        else:
            print("Opção inválida!")





