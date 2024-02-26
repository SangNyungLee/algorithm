import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input().rstrip())
graph = [[INF] * n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == b:
            graph[a][b] = 0

for i in range(n):
    gg = list(map(int, input().split(" ")))
    for j in range(n):
        if gg[j] == 0:
            graph[i][j] = INF
        else:
            graph[i][j] = gg[j]

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n):
    for b in range(n):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()


############ BFS ###################
import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
graph = []
result = [[0] * n for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(start):
    queue = deque()
    visited = [False] * (n)
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for i in range(n):
            if not visited[i] and graph[cur][i]:
                result[start][i] = 1
                visited[i] = True
                queue.append(i)


for i in range(n):
    bfs(i)

for i in result:
    print(*i)


################### DFS ######################
import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().split())) for _ in range(n)]


def dfs(start):
    for i in range(n):
        if not visited[i] and graph[start][i]:
            visited[i] = True
            dfs(i)


for i in range(n):
    visited = [False] * n
    dfs(i)
    for j in visited:
        if not j:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()
