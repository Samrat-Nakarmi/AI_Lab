from collections import deque

def water_jug_bfs(jug1_capacity, jug2_capacity, target):

    if target > max(jug1_capacity, jug2_capacity):
        return "No solution possible"

    queue = deque([(0, 0)])  
    visited = set((0, 0))
    

    path = {}

    while queue:
        jug1, jug2 = queue.popleft()

      
        if jug1 == target or jug2 == target:
            result = []
            while (jug1, jug2) in path:
                result.append((jug1, jug2))
                jug1, jug2 = path[(jug1, jug2)]
            result.reverse()
            return result

        
        possible_moves = [
            (jug1_capacity, jug2),                #
            (jug1, jug2_capacity),               
            (0, jug2),                           
            (jug1, 0),                            
            (jug1 - min(jug1, jug2_capacity - jug2), jug2 + min(jug1, jug2_capacity - jug2)), 
            (jug1 + min(jug2, jug1_capacity - jug1), jug2 - min(jug2, jug1_capacity - jug1))  
        ]


        for next_jug1, next_jug2 in possible_moves:
            if (next_jug1, next_jug2) not in visited:
                queue.append((next_jug1, next_jug2))
                visited.add((next_jug1, next_jug2))
                path[(next_jug1, next_jug2)] = (jug1, jug2)

    return "No solution found."


jug1_capacity = 4 
jug2_capacity = 3 
target = 2         
solution = water_jug_bfs(jug1_capacity, jug2_capacity, target)
print("Solution path:", solution)
