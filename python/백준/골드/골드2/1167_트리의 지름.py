############# 다익스트라 알고리즘 ############
import sys

input = sys.stdin.readline
import heapq

n = int(input())
INF = int(1e9)
graph = [[] for _ in range(n + 1)]
for k in range(1, n + 1):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1, 2):
        graph[arr[0]].append((arr[i], arr[i + 1]))
distance = [INF] * (n + 1)


# 1부터 시작
def dijkstra(start):
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


dijkstra(1)
distance[0] = -1
idx = distance.index(max(distance))
distance = [INF] * (n + 1)
dijkstra(idx)
distance[0] = -1
print(max(distance))

############## BFS 알고리즘 ##################
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
for k in range(1, n + 1):
    arr = list(map(int, input().split()))
    for i in range(1, len(arr) - 1, 2):
        graph[arr[0]].append((arr[i], arr[i + 1]))
visited = [-1] * (n + 1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        x = queue.popleft()
        for a, b in graph[x]:
            if visited[a] == -1:
                visited[a] = visited[x] + b
                queue.append(a)


bfs(1)
idx = visited.index(max(visited))
visited = [-1] * (n + 1)
bfs(idx)
print(max(visited))
