from collections import deque
import sys

input = sys.stdin.readline

# N = 정점의 개수, M = 간선의 개수
N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


def bfs():
    global result
    while queue:
        cur = queue.popleft()
        for i in range(N + 1):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                queue.append(i)
    result += 1


result = 0
queue = deque([])
for i in range(1, N + 1):
    if visited[i] == False:
        queue.append(i)
        visited[i] = True
        bfs()
print(result)
