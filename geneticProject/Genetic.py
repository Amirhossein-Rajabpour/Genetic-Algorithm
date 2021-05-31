class Genetic:
    # population is dictionary between generation and object array of chromosome
    # => {1: [chromosome1, chromosome2, ...], 2:[chromosomeK, ...]}
    def __init__(self, population, game_plate):
        self.population = population
        self.game_plate = game_plate

