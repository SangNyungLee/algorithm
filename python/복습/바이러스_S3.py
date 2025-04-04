from collections import deque

n = int(input())
m = int(input())
graph = [[False] * (n + 1) for _ in range (n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

count = 0
def bfs():
    global count
    queue = deque()
    queue.append(1)
    visited[1] = True
    while queue:
        cur = queue.popleft()
        for i in range(1, n + 1):
            if not visited[i] and graph[i][cur]:
                visited[i] = True
                count += 1
                queue.append(i)

bfs()
print(count)
