# Simple A* Algorithm

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3},
    'C': {'D': 1},
    'D': {}
}

heuristic = {
    'A': 4,
    'B': 2,
    'C': 1,
    'D': 0
}

start = 'A'
goal = 'D'

current = start

path = [current]

while current != goal:

    min_cost = 999

    next_node = ""

    for node in graph[current]:

        cost = graph[current][node] + heuristic[node]

        if cost < min_cost:

            min_cost = cost
            next_node = node

    current = next_node

    path.append(current)

print("Shortest Path is :")

for i in path:
    print(i, end=" ")