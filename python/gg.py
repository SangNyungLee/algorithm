import heapq

V, E = map(int, input().split())
start = int(input())
INF = int(1e9)
distance = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for next_node, weight in graph[now]:
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

dijkstra(start)
print(distance)