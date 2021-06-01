# from geneticProject.AdditionalFunctions import *
from Genetic import *
from AdditionalFunctions import *
from GraphicalUserInterface import *
# from geneticProject.Genetic import *

generation_dict = {}


def get_input_from_user():
    test_case = input("Enter your level: ")
    test_case_file_name = test_case + ".txt"
    num_of_population = input("Enter the amount of population: ")
    score_mode = input("Enter score mode:\n0) Without calculating winning points\n1) With calculating winning points\n")
    selection_mode_input = input("Enter selection mode:\n1) Weighted random selection\n2) Best selection\n")
    if selection_mode_input == '1':
        selection_mode = 'random'
    elif selection_mode_input == '2':
        selection_mode = 'best'
    else:
        print('Wrong selection mode input!')
        exit()

    crossover_mode_input = input("Enter crossover mode:\n1) Random crossover\n2) Specified crossover\n")
    if crossover_mode_input == '1':
        crossover_mode = 'random'
        crossover_point = 0

    elif crossover_mode_input == '2':
        crossover_mode = 'specified'
        crossover_point = int(input('Enter crossover point: \n'))
    else:
        print('Wrong crossover mode input!')
        exit()

    mutation_prob = input("Enter mutation probability: \n")
    return test_case_file_name, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, float(mutation_prob)
    # return "level8.txt", "100", "1", "random", "random", 0, 0.1




    # TO DO: call graphical interface code

    # TO DO: plot average scores per generation
    generation_average_scores = genetic.generation_average_scores
    generation_max_scores = genetic.generation_max_score
    generation_min_scores = genetic.generation_min_score


def start_genetic_algorithm(game_plate, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob):

    initial_population = generate_initial_population(int(num_of_population), game_plate, score_mode)
    generations = {1: initial_population}
    genetic = Genetic(generations, game_plate, selection_mode, crossover_mode, crossover_point, mutation_prob, score_mode)

    return genetic


if __name__ == "__main__":
    test_case_file_name, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob = get_input_from_user()
    game_plate_str = read_level_game(test_case_file_name)
    result_genetic_algorithm = start_genetic_algorithm(game_plate_str, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob)

    result_path_str = result_genetic_algorithm.best_answer.string
    if result_path_str != "":
        print("goal chromosome path is : {}".format(result_path_str))
        print("goal chromosome generation : {}".format(result_genetic_algorithm.best_answer.generation))
        print("goal chromosome scores : {}".format(result_genetic_algorithm.best_answer.score))



        # render GUI
        game_plate_arr = create_game_plate_arr(game_plate_str)
        super_mario_movements = get_sequence_movement(result_path_str, game_plate_arr)
        game = GraphicalUserInterface(super_mario_movements)
        game.Visualize()

    else:
        print("not found")
