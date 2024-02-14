from collections import deque


def solution(land):
    n = len(land)  # 세로 (5)
    m = len(land[0])  # 가로 (8)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = [[0] for _ in range(m)]
    visited = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and not visited[i][j]:
                count = []
                queue = deque()
                queue.append((i, j))
                count.append((i, j))
                visited[i][j] = True
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or ny < 0 or nx >= n or ny >= m:
                            continue
                        if land[nx][ny] == 1 and not visited[nx][ny]:
                            visited[nx][ny] = True
                            count.append((nx, ny))
                            queue.append((nx, ny))
                cnt = len(count)
                unique = set(y for x, y in count)
                for g in unique:
                    result[g][0] += cnt
    answer = max(result)
    return answer[0]
