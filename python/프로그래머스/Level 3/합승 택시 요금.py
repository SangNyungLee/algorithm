def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    distance = [INF] * (n + 1)
    for i in range(1, n + 1):
        graph[i][i] = 0

    for q, w, e in fares:
        graph[q][w] = e
        graph[w][q] = e

    for k in range(1, n + 1):
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

    for i in range(1, n + 1):
        distance[i] = graph[s][i] + graph[i][a] + graph[i][b]
    return min(distance)


#################### 다익스트라 알고리즘 ################
import heapq


def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[] for _ in range(n + 1)]
    result = []
    for qq in range(1, n + 1):
        graph[qq].append((qq, 0))
    for q, w, e in fares:
        graph[q].append((w, e))
        graph[w].append((q, e))

    for p in range(1, n + 1):
        distance = [INF] * (n + 1)
        visited = [False] * (n + 1)
        queue = []
        heapq.heappush(queue, (0, p))
        visited[p] = True
        while queue:
            dist, now = heapq.heappop(queue)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue, (cost, i[0]))
        result.append(distance[1::])
    MIN = 400000000
    for pp in range(1, n + 1):
        MIN = min(MIN, result[s - 1][pp] + result[pp - 1][a] + result[pp - 1][b])
    return MIN
