import random, math
from geneticProject.AdditionalFunctions import *


class Chromosome:
    def __init__(self, string, score, generation, failure_points):
        self.string = string
        self.score = score
        self.generation = generation
        self.failure_points = failure_points

    def update_score_failurepoints(self, new_score, new_failurepoints):
        self.score = new_score
        self.failure_points = new_failurepoints


def selection(len_population, array_of_new_chromosomes, array_of_prev_chromosomes, selection_mode):
    # 70% of new population is from new chormosomes (children of previous layer)
    # 30% of new population is from chromosomes in the previous layer
    next_generation = []
    next_generation += array_of_new_chromosomes

    # randomly (with their scores as their weights) select from previous generation
    if selection_mode == 'random':
        score_weights = return_scores(array_of_prev_chromosomes)
        next_generation += random.choices(list(array_of_prev_chromosomes), weights=score_weights,k=math.ceil(len_population * 0.3))
    
    # sort array_of_prev_chromosomes and take top chromosomes
    elif selection_mode == 'best':
        sorted_array_of_prev_chromosomes = sort_by_score(array_of_prev_chromosomes)
        next_generation += sorted_array_of_prev_chromosomes[:math.ceil(len_population * 0.3)]

    return next_generation


def crossover(chromosome1, chromosome2, crossover_point, crossover_mode):
    # caution: chromosomes are objects here not their strings!
    offspring1, offspring2 = [], []
    chromosome_length = len(chromosome1.string)

    if crossover_mode == 'random':
        crossing_point = random.randint(0, chromosome_length - 1)
        offspring1 = chromosome1.string[:crossing_point] + chromosome2.string[crossing_point:]
        offspring2 = chromosome2.string[:crossing_point] + chromosome1.string[crossing_point:]

    elif crossover_mode == 'specified':
        offspring1 = chromosome1.string[:crossover_point] + chromosome2.string[crossover_point:]
        offspring2 = chromosome2.string[:crossover_point] + chromosome1.string[crossover_point:]

    return offspring1, offspring2


def mutation(chromosome, mutatiom_probability, game):
    chromosome_failure_points = chromosome.failure_points
    for f_point_index in chromosome_failure_points:
        if random.random() < mutatiom_probability:
            # it mutate a failure character.
            new_value = str((int(chromosome.string[f_point_index]) + 1) % 3)
            left_part = chromosome.string[:f_point_index]
            right_part = chromosome.string[f_point_index+1:]

            chromosome.string = left_part + new_value + right_part

            new_score, new_failurepoints = game.get_score(chromosome.string, "")
            chromosome.update_score_failurepoints(new_score, new_failurepoints)