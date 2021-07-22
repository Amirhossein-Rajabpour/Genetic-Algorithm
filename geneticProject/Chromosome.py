class Chromosome:
    def __init__(self, string, score, generation, failure_points):
        self.string = string
        self.score = score
        self.generation = generation
        self.failure_points = failure_points