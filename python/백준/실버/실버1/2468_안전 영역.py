import sys
import copy
from collections import deque
# input = sys.stdin.readline

N = int(input())
graph=[]
q =[]

for i in range(N):
    graph.append(list(map(int, input().split())))
maxNum = max(max(graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph2[nx][ny] != 0:
                graph2[nx][ny] = 0
                queue.append((nx,ny))
    return 1
for k in range(1, maxNum+1):
    result = 0
    graph2 = copy.deepcopy(graph)
    visited = [False] * (N**2)
    for i in range(N):
        for j in range(N):
            if graph2[i][j] != 0 and graph2[i][j] > k:
                result += bfs(i,j)
    q.append(result)
print(q)
print(max(q))