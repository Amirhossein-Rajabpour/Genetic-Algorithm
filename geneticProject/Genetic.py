from geneticProject.AdditionalFunctions import *
from geneticProject.Chromosome import *

def is_end():
    pass

def calculate_average_score(array_of_chromosomes):
    sum_scores = 0
    for chromosome in array_of_chromosomes:
        sum_scores += chromosome.score
    return sum_scores/len(array_of_chromosomes)

def choose_two_parents(array_of_chromosomes):
    parent1, parent2 = random.sample(array_of_chromosomes, 2)
    return parent1, parent2


class Genetic:
    # population is a dictionary of generation and array of chromosome objects
    # => {1: [chromosome1, chromosome2, ...], 2:[chromosomeK, ...]}
    def __init__(self, population, game_plate, selection_mode, crossover_mode, crossover_point):
        self.population = population
        self.game_plate = game_plate
        self.selection_mode = selection_mode
        self.crossover_mode = crossover_mode
        self.crossover_point = crossover_point
        self.best_answer = ''
        self.generation_average_scores = {}

        current_generation = 2
        len_population = len(self.population[1])
        self.generation_average_scores[1] = calculate_average_score(sort_by_score(self.population[1])[:math.ceil(len_population * 0.5)])

        while not is_end():

            # crossover step
            new_generation, new_generation_strings = [], []
            while True:
                # half of the population which is better than the other half is chosen and 70% of the new generation are children of this half
                parent1, parent2 = choose_two_parents(self.population[current_generation-1])
                child1, child2 = crossover(parent1, parent2, self.crossover_point, self.crossover_mode)
                game = Game(self.game_plate)

                if child1 not in new_generation_strings:
                    score1, failure_points1 = game.get_score(child1, score_mode="")
                    new_generation.append(Chromosome(child1, score1, current_generation, failure_points1))
                    new_generation_strings.append(child1)
                if len(new_generation_strings) == math.ceil(len_population * 0.7):
                    break

                if child2 not in new_generation_strings:
                    score2, failure_points2 = game.get_score(child2, score_mode="")
                    new_generation.append(Chromosome(child2, score2, current_generation, failure_points2))
                    new_generation_strings.append(child2)
                if len(new_generation_strings) == math.ceil(len_population * 0.7):
                    break


            # selection step
            self.population[current_generation] = selection(len_population, new_generation, self.population[current_generation-1], self.selection_mode)

            # mutation step
            for chromosome in self.population[current_generation]:
                mutation(chromosome, 0.1, game)

            self.generation_average_scores[current_generation] = calculate_average_score(self.population[current_generation])
            
            current_generation += 1
