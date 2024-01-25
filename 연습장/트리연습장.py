import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")
    for i in range(1, N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


def bfs():
    queue.append(V)
    visited[V] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in range(1, N + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                queue.append(i)


dfs(V)
print()

visited = [False] * (N + 1)
queue = deque()

bfs()
