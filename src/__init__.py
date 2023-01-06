import sys

from tsp_encoding import TSPEncoding
from solution import Solution
from stochastic_local_search import SLS

if __name__ == '__main__':
    tsp = TSPEncoding(sys.argv[1]) # Name of the instance file.
    solution_file = sys.argv[2] # Name of the file with the best solution found.
    T = int(sys.argv[3])
    iterations = int(sys.argv[4]) # Number of iterations for stochastic local search.
    lower_bound = int(sys.argv[5]) # Lower bound for value of the best solution.

    graph = tsp.encode()
    initial_solution = Solution('1', graph) # By default the route starts from the city whose id is 1.
    route = SLS(initial_solution, T, iterations, lower_bound)
    route.run()
    route.write_solutions(solution_file)

    print('Number of cities:', graph.num_nodes)
    print('Parameter value T:', T)
    print('Total cost of the best route found:', route)
    print('Total number of iterations:', iterations)
