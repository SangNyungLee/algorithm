import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input().rstrip())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1

    def bfs(x, y):
        global result
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= m or ny >= n:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return 1

    result = 0
    for i in range(m + 1):
        for j in range(n + 1):
            if graph[i][j] == 1:
                result += bfs(i, j)
    print(result)
