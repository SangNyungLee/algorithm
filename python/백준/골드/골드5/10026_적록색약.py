import copy
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(1, N + 1):
    graph.append(list(map(str, input())))

# 적록색약
graph2 = copy.deepcopy(graph)
result = 0
result2 = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]

# 정상인
def bfs(color, x, y):
    queue = deque()
    graph[x][y] = 0
    queue.append((color,x,y))
    while queue:
        color, x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == color:
                graph[nx][ny] = 0
                queue.append((color, nx, ny))
    return 1

# 적록색약
def bfs2(color, x, y):
    queue2 = deque()
    graph2[x][y] = 0
    queue2.append((x, y))
    while queue2:
        x, y = queue2.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or graph2[nx][ny] == 0:
                continue
            if color == 'B' and graph2[nx][ny] == color:
                graph2[nx][ny] = 0
                queue2.append((nx, ny))
            if color != 'B' and graph2[nx][ny] in ['G', 'R']:
                graph2[nx][ny] = 0
                queue2.append((nx, ny))
    return 1

for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            result += bfs(graph[i][j], i,j)
        if graph2[i][j] !=0:
            result2 += bfs2(graph2[i][j],i,j)
print(result)
print(result2)
