from Genetic import *
from AdditionalFunctions import *
from GraphicalUserInterface import *
import matplotlib.pyplot as plt


generation_dict = {}


def get_input_from_user():
    # test_case = input("Enter your level: ")
    # test_case_file_name = test_case + ".txt"
    # num_of_population = input("Enter the amount of population: ")
    # score_mode = input("Enter score mode:\n0) Without calculating winning points\n1) With calculating winning points\n")
    # selection_mode_input = input("Enter selection mode:\n1) Weighted random selection\n2) Best selection\n")
    # if selection_mode_input == '1':
    #     selection_mode = 'random'
    # elif selection_mode_input == '2':
    #     selection_mode = 'best'
    # else:
    #     print('Wrong selection mode input!')
    #     exit()

    # crossover_mode_input = input("Enter crossover mode:\n1) Random crossover\n2) Specified crossover\n")
    # if crossover_mode_input == '1':
    #     crossover_mode = 'random'
    #     crossover_point = 0

    # elif crossover_mode_input == '2':
    #     crossover_mode = 'specified'
    #     crossover_point = int(input('Enter crossover point: \n'))
    # else:
    #     print('Wrong crossover mode input!')
    #     exit()

    # mutation_prob = input("Enter mutation probability: \n")
    # return test_case_file_name, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, float(mutation_prob)
    return "level8.txt", "500", "1", "random", "random", 0, 0.3




def start_genetic_algorithm(game_plate, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob):

    initial_population = generate_initial_population(int(num_of_population), game_plate, score_mode)
    generations = {1: initial_population}
    genetic = Genetic(generations, game_plate, selection_mode, crossover_mode, crossover_point, mutation_prob, score_mode)

    return genetic

def plot_results(genetic):
    generation_average_scores = genetic.generation_average_scores
    generation_max_scores = genetic.generation_max_score
    generation_min_scores = genetic.generation_min_score

    print("avg: ", generation_average_scores)
    print('max: ', generation_max_scores)
    print('min: ', generation_min_scores)

    plt.plot(*zip(*sorted(generation_average_scores.items())), color='r', label='avg scores')
    plt.plot(*zip(*sorted(generation_max_scores.items())), color='g', label='max scores')
    plt.plot(*zip(*sorted(generation_min_scores.items())), color='b', label='min scores')

    plt.xlabel('generations')
    plt.ylabel('score')
    plt.legend(loc=0)
    plt.show()


if __name__ == "__main__":
    test_case_file_name, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob = get_input_from_user()
    game_plate_str = read_level_game(test_case_file_name)
    result_genetic_algorithm = start_genetic_algorithm(game_plate_str, num_of_population, score_mode, selection_mode, crossover_mode, crossover_point, mutation_prob)

    result_path_str = result_genetic_algorithm.best_answer.string
    if result_path_str != "":
        print("String of goal chromosome: {}".format(result_path_str))
        print("Generation of goal chromosome: {}".format(result_genetic_algorithm.best_answer.generation))
        print("Score of goal chromosome: {}".format(result_genetic_algorithm.best_answer.score))
        print("failure points : {}".format(result_genetic_algorithm.best_answer.failure_points))

        # plot results
        plot_results(result_genetic_algorithm)


        # render GUI
        game_plate_arr = create_game_plate_arr(game_plate_str)
        super_mario_movements = get_sequence_movement(result_path_str, game_plate_arr)
        game = GraphicalUserInterface(super_mario_movements)
        game.Visualize()

    else:
        print("not found")
