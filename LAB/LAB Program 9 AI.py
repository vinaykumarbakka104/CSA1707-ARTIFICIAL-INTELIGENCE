
from itertools import permutations

distance = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

n = len(distance)
cities = list(range(1, n))
min_cost = float('inf')

for path in permutations(cities):
    tour = (0,) + path + (0,)
    cost = 0

    for i in range(len(tour) - 1):
        cost += distance[tour[i]][tour[i + 1]]

    if cost < min_cost:
        min_cost = cost
        best_tour = tour

print("Best Tour:", best_tour)
print("Minimum Cost:", min_cost)
