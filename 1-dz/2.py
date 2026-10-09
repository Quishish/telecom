from collections import defaultdict, deque

def find_city_with_min_reachable(n, edges, mileage):

    graph = defaultdict(list)
    for city_a, city_b, distance in edges:
        graph[city_a].append((city_b, distance))
        graph[city_b].append((city_a, distance))
    
    min_reachable = float('inf')
    best_city = -1

    for city in range(n):
        reachable_count = 0
        visited = {city}
        queue = deque([(city, 0)])
        
        while queue:
            current, dist = queue.popleft()
            
            for neighbor, weight in graph[current]:
                new_dist = dist + weight
                if neighbor not in visited and new_dist <= mileage:
                    visited.add(neighbor)
                    reachable_count += 1
                    queue.append((neighbor, new_dist))
        
        if reachable_count < min_reachable:
            min_reachable = reachable_count
            best_city = city
    
    return best_city, min_reachable

if __name__ == "__main__":
    edges = [
        [0, 1, 10],
        [0, 2, 5],
        [1, 2, 3],
        [1, 3, 8],
        [2, 3, 7],
        [3, 4, 15]
    ]
    
    mileage = 12
    
    best_city, min_count = find_city_with_min_reachable(5, edges, mileage)
    print(f"Город {best_city} имеет наименьшее число достижимых городов: {min_count}")