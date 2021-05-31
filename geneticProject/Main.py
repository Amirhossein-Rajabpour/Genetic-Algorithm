from geneticProject.AdditionalFunctions import *
from geneticProject.Genetic import *
generation_dict = {}

def main():
    test_case = input("Enter your level: ")
    test_case_file_name = test_case + ".txt"
    num_of_population = input("Enter the amount of population: ")
    score_mode = input("Enter score mode:\n0) Without calculating winning points\n1) With calculating winning points\n")

    game_plate = read_level_game(test_case_file_name)
    initial_population = generate_initial_population(num_of_population, game_plate, score_mode)

    selection_mode_input = input("Enter selection mode:\n1) Weighted random selection\n2) Best selection\n")
    if selection_mode_input == '1':
        selection_mode = 'random'
    elif selection_mode_input == '2':
        selection_mode = 'best'
    else:
        print('Wrong selection mode input!')
        exit()

    crossover_mode = input("Enter crossover mode:\n1) Random crossover\n2) Specified crossover\n")
    if selection_mode_input == '1':
        selection_mode = 'random'
        crossover_point = 0
    elif selection_mode_input == '2':
        selection_mode = 'specified'
        crossover_point = int(input('Enter crossoverpoint: \n'))
    else:
        print('Wrong crossover mode input!')
        exit()

    genetic = Genetic(initial_population, game_plate, selection_mode, crossover_mode, crossover_point)
    final_answer = genetic.best_answer

    # TO DO: call graphical interface code



if __name__ == "__main__":
    main()












