from queue import PriorityQueue

def greedy_best_first_search(graph, start, goal, heuristic):
    open_set = PriorityQueue()
    open_set.put((heuristic[start], start))
    visited = set()

    while not open_set.empty():
        _, current = open_set.get()
        if current in visited:
            continue

        print(current, end=" ") 
        visited.add(current)

        if current == goal:
            print("\nGoal reached!")
            return

        for neighbor in graph[current]:
            if neighbor not in visited:
                open_set.put((heuristic[neighbor], neighbor))  

    print("\nGoal not reachable.")


    

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 1,
    'E': 2,
    'F': 0
}

print("Greedy Best-First Search:")
greedy_best_first_search(graph, 'A', 'F', heuristic)

