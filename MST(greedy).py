# Minimum Spanning Tree using Prim's Algorithm

graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

selected = [0, 0, 0, 0, 0]

selected[0] = 1

edge = 0

print("Edges in Minimum Spanning Tree :\n")

while edge < 4:

    minimum = 999

    x = 0
    y = 0

    for i in range(5):

        if selected[i] == 1:

            for j in range(5):

                if selected[j] == 0 and graph[i][j] != 0:

                    if graph[i][j] < minimum:

                        minimum = graph[i][j]

                        x = i
                        y = j

    print(x, "-", y, "=", graph[x][y])

    selected[y] = 1

    edge += 1