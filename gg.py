import sys
import heapq

input = sys.stdin.readline

INF = int(1e9)
V, E = map(int, input().split())
K = int(input().rstrip())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            # i에는 i[0] : 내가 가는 곳이랑 i[1] : 거기까지의 거리가 적혀있음
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


djikstra(K)
for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
