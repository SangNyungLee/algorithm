import sys
from collections import deque
input = sys.stdin.readline

M,N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while tomato:
        x, y = tomato.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                tomato.append((nx,ny))
                graph[nx][ny] = graph[x][y] + 1

tomato = deque() # 익어있는 토마토
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i,j))
            
# 토마토가 전부 0인 경우
if not tomato:
    print(-1)
else:
    bfs()
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                tomato.append(-1)
                break
    if tomato:
        print(tomato.popleft())
    else:
        print(max(map(max, graph))-1)