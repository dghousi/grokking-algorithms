# Problem 6.1: Shortest Path from START to FINISH

from collections import deque

def bfs_shortest_path(graph, start, finish):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        vertex, path = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor == finish:
                return path + [neighbor]
            queue.append((neighbor, path + [neighbor]))

    return None

# Define the graph for Problem 6.1
graph_6_1 = {
    'START': ['S'],
    'S': ['A', 'B', 'C'],
    'A': ['F'],
    'B': ['F'],
    'C': ['F'],
    'F': [],
}

# Find the shortest path
shortest_path_6_1 = bfs_shortest_path(graph_6_1, 'START', 'F')
print("Shortest path from START to FINISH:", shortest_path_6_1)