from Chromosome import *
from Game import *
import random
import math


# continuous two "2" movement is ok but continuous three "2" movement isn't ok!
# continuous two "1" movement isn't ok
def check_game_roles(current_string, new_char):
    res = True
    if len(current_string) >= 1 and new_char == "1" and current_string[-1] == "1":
        res = False
    elif len(current_string) >= 2 and new_char == "2" and current_string[-1] == "2" and current_string[-2] == "2":
        res = False

    return res


def generate_randomly_string(length):
    string, i = "", 0
    while i < length:
        random_number = random.randint(1, 10)
        char = ""
        # probability 50 => select "0" (move right),
        # probability 30 => select "1" (jump and move right),
        # probability 20 => select "2" (dodge and move right)
        if random_number <= 5:
            char = "0"
            i += 1
        elif 5 < random_number <= 8:
            if check_game_roles(string, "1"):
                char = "1"
                i += 1
        elif 8 < random_number <= 10:
            if check_game_roles(string, "2"):
                char = "2"
                i += 1
        string += char

    return string


def read_level_game(test_case_name):
    path = "./attachments/levels/" + test_case_name
    with open(path, 'r') as file:
        game_plate = file.readline()

    return game_plate


def generate_initial_population(number_of_population, game_plate_string, score_mode):
    game = Game(game_plate_string)
    chromosome_length = len(game_plate_string)
    array_of_chromosome = []
    for i in range(number_of_population):
        chromosome_string = generate_randomly_string(chromosome_length)
        chromosome_score = game.get_score(chromosome_string, score_mode)
        chromosome = Chromosome(chromosome_string, chromosome_score, 1)
        array_of_chromosome.append(chromosome)

    return array_of_chromosome


def sort_by_score(array_of_chromosomes):
    # sort by their scores
    # return sorted array
    return array_of_chromosomes.sort(key=lambda x: x.score, reverse=False)


def selection(population, array_of_new_chromosomes, array_of_prev_chromosomes):
    # 70% of new population is from new chormosomes (children of previous layer)
    # 30% of new population is from chromosomes in the previous layer
    next_generation = []

    # sort array_of_prev_chromosomes and take top chromosomes
    sorted_array_of_prev_chromosomes = sort_by_score(array_of_prev_chromosomes)
    for chromosome in sorted_array_of_prev_chromosomes[:math.ceil(population * 0.3)]:
        next_generation.append(chromosome)

    sorted_array_of_new_chromosomes = sort_by_score(array_of_new_chromosomes)
    for chromosome in sorted_array_of_new_chromosomes[:math.ceil(population * 0.7)]:
        next_generation.append(chromosome)

    return next_generation
