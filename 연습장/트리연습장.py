import sys
from collections import deque

input = sys.stdin.readline

# 입력값 받기
R, C = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]

# 상하좌우 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    queue = deque()
    queue.append((x, y, graph[x][y]))
    max_count = 1

    while queue:
        x, y, path = queue.popleft()
        max_count = max(max_count, len(path))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] not in path:
                queue.append((nx, ny, path + graph[nx][ny]))

    return max_count


print(bfs(0, 0))
