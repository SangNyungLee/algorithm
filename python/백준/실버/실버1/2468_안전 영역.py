import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = []
q = []

for i in range(N):
    graph.append(list(map(int, input().split())))
maxNum = max(map(max, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, graph2):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph2[nx][ny] != 0:
                graph2[nx][ny] = 0
                queue.append((nx, ny))
    return 1


for k in range(0, maxNum + 1):
    result = 0
    for p in graph:
        graph2 = [[0 if element <= k else element for element in row] for row in graph]
    for i in range(N):
        for j in range(N):
            if graph2[i][j] != 0 and graph2[i][j] > k:
                result += bfs(i, j, graph2)
    q.append(result)
print(max(q))


###############################

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
