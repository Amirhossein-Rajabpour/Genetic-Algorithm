import random
from AdditionalFunctions import *

class Chromosome:
    def __init__(self, string, score, generation):
        self.string = string
        self.score = score
        # self.failure_points = failure_points
        self.generation = generation


def selection(population, array_of_new_chromosomes, array_of_prev_chromosomes, selection_mode):
    # 70% of new population is from new chormosomes (children of previous layer)
    # 30% of new population is from chromosomes in the previous layer
    next_generation = []

    # sort array_of_prev_chromosomes and take top chromosomes
    sorted_array_of_prev_chromosomes = sort_by_score(array_of_prev_chromosomes)
    next_generation += sorted_array_of_prev_chromosomes[:math.ceil(population * 0.3)] 

    if selection_mode == 'random':
        score_weights = return_scores(array_of_new_chromosomes)
        next_generation += random.choices(list(array_of_new_chromosomes), weights=score_weights, k=math.ceil(population * 0.7))

    elif selection_mode == 'best':
        sorted_array_of_new_chromosomes = sort_by_score(array_of_new_chromosomes)
        next_generation += sorted_array_of_new_chromosomes[:math.ceil(population * 0.7)]

    return next_generation


def cross_over(chromosome1, chromosome2, crossover_point, crossover_mode):
    # caution: chromosomes are objects here not their strings!
    offspring1, offspring2 = [], []
    chromosome_length = len(chromosome1.string)

    if crossover_mode == 'random':
        crossing_point = random.randint(0,chromosome_length-1)
        offspring1 = chromosome1.string[:crossing_point] + chromosome2.string[crossing_point:]
        offspring2 = chromosome2.string[:crossing_point] + chromosome1.string[crossing_point:]

    elif crossover_mode == 'specified':
        offspring1 = chromosome1.string[:crossover_point] + chromosome2.string[crossover_point:]
        offspring2 = chromosome2.string[:crossover_point] + chromosome1.string[crossover_point:]

    # TO DECIDE: here children are strings. but it's better to create their chromosome object here and return the objects
    return offspring1, offspring2


def mutation(chromosome, mutatiom_probability):
    chromosome_length = len(chromosome.string)
    if random.random() < mutatiom_probability:
        # it can flip a random bit or it can flip a specified bit.
        chromosome.string[random.randint(0,chromosome_length-1)]