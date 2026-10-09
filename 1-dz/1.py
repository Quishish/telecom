import heapq
from collections import defaultdict

def min_bottleneck_path(n, edges, start, end):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    bottleneck = [float('inf')] * n
    bottleneck[start] = 0

    pq = [(0, start)]
    
    while pq:
        current_bottleneck, u = heapq.heappop(pq)

        if current_bottleneck > bottleneck[u]:
            continue

        if u == end:
            return current_bottleneck

        for v, weight in graph[u]:
            new_bottleneck = max(current_bottleneck, weight)
            
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