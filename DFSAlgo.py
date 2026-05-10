# DFS Using Recurssion

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

def dfs(node):
    if node not in visited:
        print(node)
        visited.append(node)

    for i in graph[node]:
        dfs(i)

dfs('A')    