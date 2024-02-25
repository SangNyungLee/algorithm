################ 플로이드-워셜 알고리즘 사용 ############
import sys

input = sys.stdin.readline
INF = int(1e9)
n = int(input().rstrip())
m = int(input().rstrip())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()


########### 다익스트라 사용 ####################
import sys
import heapq

input = sys.stdin.readline
v = int(input().rstrip())
e = int(input().rstrip())
graph = [[] for _ in range(v + 1)]
INF = int(1e9)
for _ in range(e):
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
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))


for i in range(1, v + 1):
    distance = [INF] * (v + 1)
    djikstra(i)
    for j in range(1, v + 1):
        if distance[j] == INF:
            print(0, end=" ")
        else:
            print(distance[j], end=" ")
    print()
