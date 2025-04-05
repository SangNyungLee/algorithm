from collections import deque
import copy

n,m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input())))
graph[0][0] = 1

def bfs(graph):
    queue = deque()
    queue.append((0,0,0, graph)) # 제일 마지막거는 내가 벽을 한 번이라도 뚫었는지 안 뚫었는지 체크하는거
    while queue:
        x,y,wall = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 앞으로 가려고 하는 곳이 만약에 벽인데 내 wall 값이 0이면 벽 녹여버림
            if wall == 0:
                graph[nx][ny] = 0
                wall = 1
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny, wall, graph))
    return graph[n -1][m - 1]

bfs(graph)