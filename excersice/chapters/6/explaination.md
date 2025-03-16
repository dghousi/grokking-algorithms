### Explanation

- **BFS Function**: The `bfs_shortest_path` function finds the shortest path from a start node to a finish node using breadth-first search.
- **Graph Representation**: The graphs for both problems are represented as dictionaries, where keys are nodes and values are lists of adjacent nodes.
- **Output**: The program prints the shortest paths for both problems.

### Code explaination review:

1. **`queue = deque([(start, [start])])`**:

- This line initializes a queue using `deque` (a double-ended queue from the `collections` module).
- It starts the queue with a tuple containing the start node and a list that tracks the path taken to reach that node (initially just the start node itself).
- The purpose of this queue is to store nodes to be explored, along with the paths leading to them.

2. **`visited = set()`**:

- This line initializes an empty set called `visited`.
- The `visited` set is used to keep track of the nodes that have already been explored.
- By marking nodes as visited, the algorithm avoids processing the same node multiple times, which helps prevent infinite loops and reduces unnecessary computations.

These two commands are essential for implementing the breadth-first search algorithm effectively. The queue allows for exploring nodes level by level, while the visited set ensures each node is processed only once.

3. **`while queue:`**

   - This starts a loop that continues as long as there are elements in the `queue`. Each iteration processes one element from the queue.

4. **`vertex, path = queue.popleft()`**

   - This line retrieves and removes the leftmost element from the `queue`, which is a tuple containing:
     - `vertex`: the current node being explored.
     - `path`: the list of nodes visited to reach this `vertex`.
   - Using `popleft()` ensures that nodes are processed in the order they were added (FIFO), characteristic of breadth-first search.

5. **`if vertex in visited:`**

   - This checks if the current `vertex` has already been visited.
   - If it has, the algorithm skips the rest of the loop for this iteration using `continue`, preventing reprocessing of the same node.

6. **`visited.add(vertex)`**

   - If the `vertex` has not been visited, it is added to the `visited` set to mark it as explored.

7. **`for neighbor in graph[vertex]:`**

   - This iterates over all neighboring nodes (adjacent nodes) of the current `vertex`, as defined in the `graph`.

8. **`if neighbor == finish:`**

   - This checks if the current neighbor is the target `finish` node.
   - If it is, the function returns the complete path taken to reach it by concatenating the current `path` with the `neighbor`.

9. **`queue.append((neighbor, path + [neighbor]))`**
   - If the neighbor is not the finish node, a new tuple is appended to the `queue`. This tuple contains:
     - `neighbor`: the adjacent node to explore next.
     - `path + [neighbor]`: a new path that includes the current path plus the neighbor, keeping track of the route taken.

### Summary

This block of code effectively explores each node in the graph, tracks the path taken to reach each node, checks for the target node, and manages the exploration of neighboring nodes while avoiding cycles by using the `visited` set. It implements the core logic of breadth-first search to find the shortest path in an unweighted graph.

<br>

![Breadth First Search](./assets/bfs-search.png)
