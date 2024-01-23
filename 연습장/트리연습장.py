import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())
graph = [[0] * M for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(min(a, c), max(a, c)):
        for j in range(min(b, d), max(b, d)):
            graph[i][j] = 1


def bfs(i, j):
    queue.append((i, j))
    graph[i][j] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                queue.append((nx, ny))
                graph[nx][ny] = 1
                cnt += 1
    return cnt


num = 0  # 영역의 개수
result = []
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            num += 1
            result.append(bfs(i, j))
result.sort()
print(num)
for i in result:
    print(i, end=" ")
