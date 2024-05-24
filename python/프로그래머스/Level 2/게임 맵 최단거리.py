from collections import deque


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    n = len(maps[0])
    m = len(maps)
    visited = [[False] * n for _ in range(m)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if maps[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1
    if visited[m - 1][n - 1] == False:
        return -1
    else:
        return maps[m - 1][n - 1]
