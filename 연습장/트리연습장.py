import sys
from collections import deque

input = sys.stdin.readline


# 3. bfs함수 구현
def bfs(x, y, high):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] > high and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


# 1. 입력값 받기
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
# 최대 높이값 구하기
high = max(map(max, graph))
# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

MAX = 0
# 2. 수심에 따라 달라지는 안전영역 갯수 비교
for t in range(high):
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > t and visited[i][j] == 0:
                visited[i][j] = 1  # 방문표시
                bfs(i, j, t)
                cnt += 1
    if MAX < cnt:
        MAX = cnt
print(MAX)
