import sys
from collections import deque
<<<<<<< HEAD
input = sys.stdin.readline

n,m,v = map(int , input().split())
graph = [[0] * (n + 1)for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

=======

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[False] * (n + 1) for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i]:
            dfs(i)


>>>>>>> 4b747d5b9f3836d7b8d1369cc97b14f8de0bbbe5
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        cur = queue.popleft()
        print(cur, end=" ")
        for i in range(1, n + 1):
            if not visited[i] and graph[cur][i]:
                queue.append(i)
                visited[i] = True
<<<<<<< HEAD
def dfs(start):
    visited[start] = True
    print(start, end=" ")
    for i in range(1, n + 1):
        if not visited[i] and graph[start][i]:
            dfs(i)
=======

>>>>>>> 4b747d5b9f3836d7b8d1369cc97b14f8de0bbbe5

dfs(v)
print()
visited = [False] * (n + 1)
<<<<<<< HEAD
bfs(v)
=======
bfs(v)
>>>>>>> 4b747d5b9f3836d7b8d1369cc97b14f8de0bbbe5
