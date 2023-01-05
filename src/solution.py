from random import randrange, sample

class Solution:
    """A solution to the TSP problem."""
    def __init__(self, starting_city, graph):
        starting_city = graph.obtain_node(starting_city)
        self.cities = graph
        self.route = [starting_city]
        temp = list(graph.cities.values())
        temp.remove(starting_city)

        for _ in range(len(temp)):
            num = randrange(0, len(temp))
            self.route.append(temp[num])
            temp.remove(temp[num])

        self.route.append(starting_city)
    
    def next_solution(self):
        """Returns the next solution. 2-OPT is used."""
        next_solution = Solution(self.route[0].id, self.cities)
        new_route = next_solution.route

        # We get 4 different random numbers to do the 2-exchange.
        random_numbers = sample(range(1, len(new_route)-1), 4)
        num1, num2 = random_numbers[0], random_numbers[1]
        num3, num4 = random_numbers[2], random_numbers[3]

        # Exchange of the 4 cities.
        new_route[num1], new_route[num2] = new_route[num2], new_route[num1]
        new_route[num3], new_route[num4] = new_route[num4], new_route[num3]

        return next_solution
    
    def evaluate(self):
        """Evaluate this solution. Returns the total weight of the trip."""
        evaluation = 0
        temp = self.route.copy()
        a = temp.pop()

        while len(temp) != 0:
            b = temp.pop()
            evaluation += a.obtain_weight(b)
            a = b

        return evaluation
