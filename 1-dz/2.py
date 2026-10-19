import heapq
from collections import defaultdict

def find_city_with_min_reachable(n, edges, mileage):
    # Строим список смежности графа
    graph = defaultdict(list)
    for city_a, city_b, distance in edges:
        graph[city_a].append((city_b, distance))
        graph[city_b].append((city_a, distance))
    
    min_reachable = float('inf')  # Минимальное количество достижимых городов
    best_city = -1  # Город с минимальным количеством достижимых
    
    # Для каждого города находим кратчайшие пути до всех остальных
    for start_city in range(n):
        # dist[i] = кратчайшее расстояние от start_city до города i
        dist = [float('inf')] * n
        dist[start_city] = 0
        
        pq = [(0, start_city)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)

            # Пропускаем устаревшие записи в куче если текущее расстояние больше уже найденного кратчайшего
            if current_dist > dist[u]:
                continue
            
            # Проверяем всех соседей вершины u
            for neighbor, weight in graph[u]:
                new_dist = current_dist + weight
                
                # Если нашли более короткий путь до neighbor
                if new_dist < dist[neighbor]:
                    dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))
        
        # Считаем количество достижимых городов (расстояние <= mileage)
        # Исключаем сам start_city (расстояние 0)
        reachable_count = 0
        for city in range(n):
            if city != start_city and dist[city] <= mileage:
                reachable_count += 1
        
        # Обновляем лучший результат
        if reachable_count < min_reachable:
            min_reachable = reachable_count
            best_city = start_city
    
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