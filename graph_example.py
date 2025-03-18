from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = set()
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
    else:
        search_queue += graph[person]
        searched.add(person)
    return False

def dynamic_search(start_name):
    neighbors = graph[start_name]  # Get the neighbors of the starting name
    for neighbor in neighbors:
        print(f"Searching from {neighbor}...")
        if search(neighbor):
            break
    else:
        print("No mango seller found among the neighbors.")

def person_is_seller(name):
    return name[-1] == 'm'

# Start the dynamic search.
dynamic_search("you")
