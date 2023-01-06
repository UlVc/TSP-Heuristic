# Creates a random TSP sample given the desired number of cities, maximum weight and minimum weight possible

import sys

from itertools import product
from random import randint

NUM_CITIES = int(sys.argv[1])
PATH = sys.argv[2]
MIN_WEIGHT = int(sys.argv[3])
MAX_WEIGHT = int(sys.argv[4])

file = open(PATH, 'w+')

cities = []
for i in range(1, NUM_CITIES+1):
    cities.append(str(i))

combinations = [(x, y) for x in cities for y in cities if int(x) < int(y)]

file.write(' '.join(cities) + '\n')

for c in combinations:
    file.write(c[0] + ' ' + c[1] + ' ' + str(randint(MIN_WEIGHT, MAX_WEIGHT)) + '\n')

file.close()

print('Sample saved in ' + PATH + '.')
