from queue import PriorityQueue

def a_star(graph, start, goal, heuristic, costs):
    open_set = PriorityQueue()
    open_set.put((0, start)) 
    g_cost = {start: 0}  
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

        for neighbor, weight in graph[current].items():
            tentative_g_cost = g_cost[current] + weight
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                open_set.put((f_cost, neighbor))

    print("\nGoal not reachable.")
    
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 2, 'E': 5},
    'C': {'F': 3},
    'D': {},
    'E': {'F': 1},
    'F': {}
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 2,
    'F': 0
}

print("A* Search:")
a_star(graph, 'A', 'F', heuristic, graph)
