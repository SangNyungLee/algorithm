import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[a][b] = True
    graph[b][a] = True


def bfs():
    queue.append(v)
    visited[v] = True
    while queue:
        cur = queue.pop()
        print(cur, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                queue.append(i)


queue = deque([])
bfs()
