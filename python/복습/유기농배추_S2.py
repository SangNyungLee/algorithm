from collections import deque

def bfs(a,b):
    global count
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count += 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if (graph[nx][ny] == 1):
                graph[nx][ny] = 0
                queue.append((nx, ny))

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * (n) for _ in range(m)]
    count = 0
    for _ in range(k):
        a,b = map(int, input().split())
        graph[a][b] = 1
    
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                bfs(i,j)
    print(count)