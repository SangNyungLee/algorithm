import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs():
    queue = deque()
    queue.append((0,0))

    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
dfs()
print(graph[N-1][M-1])
