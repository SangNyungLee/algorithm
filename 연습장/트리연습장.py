from collections import deque


def solution(land):
    n = len(land)  # 세로 (5)
    m = len(land[0])  # 가로 (8)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = []
    for i in range(m):
        visited = [[False] * (m) for _ in range(n)]
        count = 0
        for j in range(n):
            if not visited[j][i] and land[j][i] == 1:
                queue = deque()
                queue.append((j, i))
                visited[j][i] = True
                count += 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            count += 1
                            queue.append((nx, ny))
        result.append(count)

    return max(result)
