import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 입력값 받기
# R = 세로, C = 가로
R, C = map(int, input().split())
graph = []
visited = [[False] * C for _ in range(R)]
alpha = []

# 아래로 출발할 때랑 오른쪽으로 출발할 때 2개로 나눠서 생각한다.
for i in range(R):
    graph.append(list(map(str, input().rstrip())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    alpha.append(graph[0][0])
    visited[0][0] = 1
    chk = 1
    while queue:
        tong = []
        chk += 1
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if not visited[nx][ny] and graph[nx][ny] not in alpha:
                visited[nx][ny] = chk
                tong.append(graph[nx][ny])
                queue.append((nx, ny))
        if tong:
            for i in set(tong):
                alpha.append(i)
    return max(map(max, visited))


print(bfs(1, 0))
print(bfs(0, 1))
