from collections import deque
import sys

input = sys.stdin.readline


def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")
    for i in range(N + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


def bfs():
    while q:
        cur = q.popleft()
        print(cur, end=" ")
        for i in range(N + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                q.append(i)


N, M, V = list(map(int, input().split()))
graph = [[False] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = list(map(int, input().split()))
    graph[a][b] = True
    graph[b][a] = True

dfs(V)
print()

visited = [False] * (N + 1)
visited[V] = True
q = deque([V])
bfs()
