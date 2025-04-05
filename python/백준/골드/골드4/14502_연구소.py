from collections import deque
from itertools import combinations
import copy
# 0 : 빈칸
# 1 : 벽
# 2 : 바이러스
# 바이러스의 개수는 2보다 크거나 같고, 10보다 작거나 같음
# 안전 영역의 최대 크기를 구하는데 이걸 어떻게 구할까
# 벽은 무조건 3개를 세워야됨
# 무조건 세워야 하는 벽을 어떤 식으로 세워야할지 고민해봐야될듯

def bfs(graph):
    lst = deque()
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 2:
                lst.append((x,y))
    count = 0
    while lst:
        x,y = lst.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if (graph[nx][ny] == 0):
                graph[nx][ny] = 2
                lst.append((nx,ny))
    for x in range(n):
        for y in range(m):
            if graph[x][y] == 0:
                count += 1
    return count

n,m = map(int, input().split())
graph = []
maxsafe = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(n):
    graph.append(list(map(int, input().split())))

queue = []
for x in range(n):
    for y in range(m):
        if graph[x][y] == 0:
            queue.append((x,y))
combi = list(combinations(queue, 3))

for (a,b),(c,d),(e,f) in combi:
    newGraph = copy.deepcopy(graph)
    newGraph[a][b] = 1
    newGraph[c][d] = 1
    newGraph[e][f] = 1
    cnt = bfs(newGraph)
    if cnt > maxsafe:
        maxsafe = cnt
        
print(maxsafe)