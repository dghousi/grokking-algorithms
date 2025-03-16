# Problem 6.1: Shortest Path from START to FINISH

from collections import deque

def bfs_shortest_path(graph, start, finish):
    queue = deque([(start, [start])])
    # This line initializes a queue using deque (a double-ended queue from the collections module).
    # It starts the queue with a tuple containing the start node and a list that tracks the path
    # taken to reach that node (initially just the start node itself).
    # The purpose of this queue is to store nodes to be explored, along with the paths
    # leading to them.

    visited = set()
    # This line initializes an empty set called visited.
    # The visited set is used to keep track of the nodes that have already been explored.
    # By marking nodes as visited, the algorithm avoids processing the same node multiple times, 
    # which helps prevent infinite loops and reduces unnecessary computations.

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