import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(idx):
    visited[idx] = True
    print(idx, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[idx][i]:
            dfs(i)


dfs(v)
