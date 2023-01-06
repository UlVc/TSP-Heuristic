# Script for making batches tests. The global variables are hardcoded, in the future it will be via command.

import matplotlib.pyplot as plt
import sys

sys.path.append('../')

from tsp_encoding import TSPEncoding
from solution import Solution
from stochastic_local_search import SLS
from statistics import stdev

ITERATIONS   = 50 # Number of iterations for each sample.
ITERATIONS_P = 100 # Number of iterations for stochastic local search.
FILES = ['../../samples/sample_11.tsp', '../../samples/sample_100.tsp', '../../samples/sample_2k.tsp'] # Path of samples
QUANTITIES = ['11', '100', '2.000'] # Number of cities for each respective copy. It serves more than anything to save graphs sizes.

def draw(T, cost, sample, t, color, sd):
    x = cost
    plt.figure(figsize=(7, 7))
    plt.hist(x, len(x), facecolor=color, alpha=0.5)
    plt.ylabel('Number of valid routes founded')
    plt.xlabel('Cost')
    plt.title(f'Solutions with T = {T}\nMinimum: {min(cost)}, Average: {sum(cost)/len(cost)}, Maximum: {max(cost)}\n$\sigma = {sd}$')
    plt.figtext(0.5, 0.01, f'Number of cities: {sample}', ha='center', fontsize=14)
    plt.savefig(f'../../samples/graphs/Iterations-{ITERATIONS}_Sample-{sample}_T-{t}.png')
    plt.show()

if __name__ == '__main__':
    cost  = [0]*ITERATIONS
    for i in range(len(FILES)):
        tsp = TSPEncoding(FILES[i])
        graph = tsp.encode()
        
        for j in range(ITERATIONS):
            initial_solution = Solution('1', graph)
            T = 0.1
            route = SLS(initial_solution, T, ITERATIONS_P, 200)
            route.run()
            cost[j] = route.solution.evaluate()
        draw(0.1,  cost, QUANTITIES[i], '01', '#4bd5f8', stdev(cost))

        for j in range(ITERATIONS):
            initial_solution = Solution('1', graph)
            T = 10
            route = SLS(initial_solution, T, ITERATIONS_P, 200)
            route.run()
            cost[j] = route.solution.evaluate()
        draw(10,  cost, QUANTITIES[i], '10', '#4b7bf8', stdev(cost))

        for j in range(ITERATIONS):
            initial_solution = Solution('1', graph)
            T = 1000
            route = SLS(initial_solution, T, ITERATIONS_P, 200)
            route.run()
            cost[j] = route.solution.evaluate()
        draw(1000,  cost, QUANTITIES[i], '1000', '#4b0ff8', stdev(cost))
