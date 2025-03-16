# Problem 6.2: Shortest Path from "cab" to "bat"
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

# Define the graph for Problem 6.2
graph_6_2 = {
    'cab': ['cat', 'car'],
    'cat': ['bat'],
    'car': ['bat'],
    'bat': [],
}

# Find the shortest path
shortest_path_6_2 = bfs_shortest_path(graph_6_2, 'cab', 'bat')
print("Shortest path from cab to bat:", shortest_path_6_2)