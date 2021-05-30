import random
import Chromosome
import math


def generate_randomly_string(length):
    string = ""
    for i in range(length):
        random_number = random.randint(1, 10)
        char = ""
        # probability 50 => select "0", probability 30 => select "1", probability 30 => select "2"
        if random_number <= 5:
            char = "0"
        elif 5 < random_number <= 8:
            char = "1"
        elif 8 < random_number <= 10:
            char = "2"
        string += char

    return string


def read_level_game(test_case_name):
    path = "./attachments/levels/" + test_case_name
    with open(path, 'r') as file:
        game_plate = file.readline()

    return game_plate


def generate_initial_population(number_of_population, chromosome_length):
    array_of_chromosome = []
    for i in range(number_of_population):
        chromosome_string = generate_randomly_string(chromosome_length)
        chromosome = Chromosome(chromosome_string, 0, [])


def sort_by_score(array_of_chromosomes):
    # sort by their scores
    # return sorted array
    pass


def selection(population, array_of_new_chromosomes, array_of_prev_chromosomes):
    # 70% of new population is from new chormosomes (children of previous layer)
    # 30% of new population is from chromosomes in the previous layer
    next_generation = []

    # sort array_of_prev_chromosomes and take top chromosomes
    sorted_array_of_prev_chromosomes = sort_by_score(array_of_prev_chromosomes)
    for chromosome in sorted_array_of_prev_chromosomes[:math.ceil(population*0.3)]:
        next_generation.append(chromosome)

    sorted_array_of_new_chromosomes = sort_by_score(array_of_new_chromosomes)
    for chromosome in sorted_array_of_prev_chromosomes[:math.ceil(population*0.7)]:
        next_generation.append(chromosome)

    return next_generation


