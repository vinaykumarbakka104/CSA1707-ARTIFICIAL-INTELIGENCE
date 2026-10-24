
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1)],
    'D': [('G', 5)],
    'E': [('G', 3)],
    'G': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'G': 0
}

open_list = [(h['A'], 0, 'A', ['A'])]
visited = set()

while open_list:
    open_list.sort()
    f, cost, node, path = open_list.pop(0)

    if node == 'G':
        print("Path:", path)
        print("Cost:", cost)
        break

    if node in visited:
        continue

    visited.add(node)

    for neighbor, weight in graph[node]:
        if neighbor not in visited:
            new_cost = cost + weight
            new_f = new_cost + h[neighbor]
            open_list.append(
                (new_f, new_cost, neighbor, path + [neighbor])
            )
