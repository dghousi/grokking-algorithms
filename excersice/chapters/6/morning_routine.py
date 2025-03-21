from collections import defaultdict, deque

class MorningRoutine:
    def __init__(self):
        self.graph = defaultdict(list)
        self.indegree = defaultdict(int)

    def add_dependency(self, task, depends_on):
        self.graph[depends_on].append(task)
        self.indegree[task] += 1
        if task not in self.indegree:
            self.indegree[task] = 0

    def topological_sort(self):
        queue = deque()
        for task in self.indegree:
            if self.indegree[task] == 0:
                queue.append(task)
        
        sorted_tasks = []
        while queue:
            current_task = queue.popleft()
            sorted_tasks.append(current_task)
            for neighbor in self.graph[current_task]:
                self.indegree[neighbor] -= 1
                if self.indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return sorted_tasks

# Create an instance of MorningRoutine
routine = MorningRoutine()

# Add dependencies based on the graph
routine.add_dependency("Exercise", "Wake up")
routine.add_dependency("Brush teeth", "Wake up")
routine.add_dependency("Pack lunch", "Wake up")
routine.add_dependency("Eat breakfast", "Brush teeth")
routine.add_dependency("Eat breakfast", "Pack lunch")
routine.add_dependency("Shower", "Exercise")
routine.add_dependency("Get dressed", "Shower")

# Get the sorted order of tasks
ordered_tasks = routine.topological_sort()

# Printing the valid tasks
print("Valid order of tasks in the morning routine:")
for task in ordered_tasks:
    print(task)