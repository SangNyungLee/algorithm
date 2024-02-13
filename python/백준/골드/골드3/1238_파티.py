import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)
N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
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


result = []
returnHome = []
djikstra(X)
for i in range(N + 1):
    returnHome.append(distance[i])
for start in range(1, N + 1):
    distance = [INF] * (N + 1)
    # start => X로 가는거
    djikstra(start)
    go = distance[X]
    result.append(go + returnHome[start])

print(max(result))
