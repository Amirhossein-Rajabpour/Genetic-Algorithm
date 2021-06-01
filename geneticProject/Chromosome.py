import random, math
from AdditionalFunctions import *


class Chromosome:
    def __init__(self, string, score, generation, failure_points):
        self.string = string
        self.score = score
        self.generation = generation
        self.failure_points = failure_points

    def update_score_failurepoints(self, new_score, new_failurepoints):
        self.score = new_score
        self.failure_points = new_failurepoints



