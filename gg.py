from collections import deque
import sys

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[i][cur]:
                queue.append(i)
                visited[i] = True


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[i][start]:
            dfs(i)


dfs(v)

visited = [False] * (n + 1)
print()
bfs(v)
