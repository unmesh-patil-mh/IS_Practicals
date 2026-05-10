graph = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

visited = []
queue = []

def bfs(start):
    visited.append(start)
    queue.append(start)

    while queue:
        node = queue.pop(0)
        print(node)

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

bfs('A')