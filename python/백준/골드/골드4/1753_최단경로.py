import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))  # (거리, 정점)
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:  # i[0] => 정점, i[1] => 거리
            cost = dist + i[1]  # cost = 정점 + 정점
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


djikstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
