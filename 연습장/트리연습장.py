import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i]:
            dfs(i)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[cur][i]:
                queue.append(i)
                visited[i] = True


dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
