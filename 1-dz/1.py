import heapq
from collections import defaultdict

def min_bottleneck_path(n, edges, start, end):
    # Строим граф: для каждой вершины список соседей и весов рёбер
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w)) # граф неориентированный
    
    # bottleneck[i] — лучшее (минимальное) узкое место пути до вершины i
    # Пока пути не найдены — ставим бесконечность
    bottleneck = [float('inf')] * n
    bottleneck[start] = 0

    pq = [(0, start)]
    
    while pq:
        current_bottleneck, u = heapq.heappop(pq)

        # Если эту вершину уже обработали с лучшим результатом — пропускаем
        if current_bottleneck > bottleneck[u]:
            continue

        # Дошли до цели - ответ найден
        if u == end:
            return current_bottleneck
        
        # Проходим по всем соседям
        for v, weight in graph[u]:
            # Узкое место нового пути = максимум из текущего и веса нового ребра
            new_bottleneck = max(current_bottleneck, weight)
            
            # Если нашли путь лучше — запоминаем и кладём в кучу
            if new_bottleneck < bottleneck[v]:
                bottleneck[v] = new_bottleneck
                heapq.heappush(pq, (new_bottleneck, v))
    
    return bottleneck[end] if bottleneck[end] != float('inf') else -1

if __name__ == "__main__":
    edges = [
        (0, 1, 10),
        (0, 2, 5),
        (1, 2, 3),
        (1, 3, 8),
        (2, 3, 7)
    ]
    
    start = 0
    end = 3
    
    result = min_bottleneck_path(4, edges, start, end)
    print(f"Минимальное узкое место пути от {start} до {end}: {result}")