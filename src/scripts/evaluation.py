# Evaluates a solution that is saved on a file

import sys

sys.path.append('../')

from solution import Solution
from tsp_encoding import TSPEncoding

if __name__ == '__main__':
    sample = sys.argv[1] # Sample of TSP problem
    solution = sys.argv[2] # Solution of the TSP sample given
    graph = TSPEncoding(sample).encode()
    route = []

    with open(solution) as file:
        while (line := file.readline().rstrip()):
            route.append(graph.obtain_node(line))

    solution = Solution('1', graph)
    solution.route = route

    print(f'Cost of the given solution: {solution.evaluate()}')
