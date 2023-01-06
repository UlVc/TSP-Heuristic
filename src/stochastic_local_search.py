from math import exp
from random import random

class SLS:
    """Implementation of Stochastic Local Search algorithm."""
    
    def __init__(self, solution, T, iterations, fee):
        self.solution = solution
        self.T = T
        self.iterations = iterations
        self.fee = fee
    
    def __str__(self):
        return str(self.solution.evaluate())

    def run(self):
        """Runs the algorithm."""

        for _ in range(self.iterations):
            if self.solution.evaluate() <= self.fee: break

            candidate_solution = self.generate_next_solution()
            delta = self.solution.evaluate() - candidate_solution.evaluate() # v_c - v_n
            try:
                e = exp(delta/self.T)
            except OverflowError:
                e = float('inf')
            probability = 1 / (1+e)

            if random() < probability: # Generates a random number in the interval [0.0, 1.0)
                self.solution = candidate_solution

    def write_solutions(self, path):
        """
        Write the obtained solution in the given path.
        :param path: File path to save the solution.
        """
        file = open(path, 'w+')
        for c in self.solution.route:
            file.write(c.id + '\n')
    
    def generate_next_solution(self):
        """Generates the next solution."""
        return self.solution.next_solution()
