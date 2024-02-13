import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
check = [[INF] * (m + 1) for _ in range(n + 1)]
graph = [[]]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

for _ in range(n):
    a = str(input().rstrip())
    graph.append(list(a))


def bfs(sx, sy):
    global result
    queue = deque()
    queue.append((sx, sy))
    check[sx][sy] = True

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= 0 or ny <= 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0 and check[nx][ny] != INF:
                check[nx][ny] = result
                queue.append((nx, ny))
    if nx == n and ny == m:
        print(result)
    else:
        result = result + 1
        for i in range(4):
            nnx = nx + dx[i]
            nny = ny + dy[i]
            if nnx <= 0 or nny <= 0 or nnx >= n or nny >= m:
                continue
            graph[nnx][nny] = 0
        bfs(nx, ny)


bfs(1, 1)
