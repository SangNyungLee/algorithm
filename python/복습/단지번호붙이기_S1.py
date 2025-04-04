from collections import deque

n = int(input())
graph = []
visited = [[False] * n for _ in range (n)]

for _ in range(n):
    graph.append(list(map(int, input())))
result = []
def bfs(x,y, visited, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    queue = deque()
    queue.append((x,y))
    visited[x][y] = True
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                graph[nx][ny] = 0
                visited[nx][ny] = True
                queue.append((nx,ny))
                count += 1
    if count:
        result.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j, visited, graph)
result.sort()
print(len(result))
for i in result:
    print(i)