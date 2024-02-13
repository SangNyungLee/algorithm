import sys
import heapq

input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())


def djikstra(start):
    distance = [INF] * (n + 1)
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))
    return distance


origin_distance = djikstra(1)
v1_distance = djikstra(v1)
v2_distance = djikstra(v2)

v1_path = origin_distance[v1] + v1_distance[v2] + v2_distance[n]
v2_path = origin_distance[v2] + v2_distance[v1] + v1_distance[n]

result = min(v1_path, v2_path)
if v1_path >= INF or v2_path >= INF:
    print(-1)
else:
    print(result)
