import heapq, sys
input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
INF = int(1e9)
distance = [INF] * (V + 1)
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

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])