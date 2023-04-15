# A heuristic for the Traveling Salesman Problem

The output of the program gives:
- Number of cities.
- Value of the parameter T, the temperature.
- Total cost of the best path found.
- Total number of iterations.

## Execution

In the src directory, use the command

> python3 __init__.py sample.tsp output.txt T iterations lower_bound

where, by order, each argument is

- Name of the input file.
- Name of the file with that will have the best solution found.
- Value of the parameter T, the temperature.
- Total iterations.
- Lower bound for value of the best solution; it stops if it finds a solution with a value better than the one indicated in this parameter.

Example:

> python3 __init__.py ../samples/sample_11.tsp ./test.txt 100 20 300

## Extra scripts

### Solution evaluation

Script that evaluates a given solution

#### Execution

Being in the src/scripts directory, execute the command

> python3 evaluacion.py sample solution

where, by order, each argument is

- File name of the sample graph.
- Name of the solution file.

### Sample generator

Script in charge of generating samples randomly.

#### Execution

Being in the src directory, the following command is executed:

> python3 scripts/sample_generator.py num_cities path minimum_weight maximum_weight 

donde, por orden, cada entrada representa

- Number of cities of the sample.
- Location to save the sample.
- Minimum weight of the graph.
- Maximum weight of the graph.

Example:

The command

> python3 scripts/sample_generator.py 10 ../samples/ex_10.tsp 1 10

will make the file ex_10.tsp containing 10 cities with random weights between 1 and 10 and it is created in the examples folder.

### TSP multiple solver

This script solves multiple given TSP problems. It also outputs graphs of the cost of some valid routes per each parameter T. In the future the script will use arguments in the command line.

To run this script, being in the src/scripts directory, run the command

> python3 tsp_solver.py
