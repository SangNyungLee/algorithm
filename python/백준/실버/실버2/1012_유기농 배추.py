from collections import deque
import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    # M : 가로길이, N : 세로길이, K : 배추가 심어져있는 위치의 개수
    M, N, K = list(map(int, input().split()))
    graph = [[0] * (N) for _ in range(M)]

    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= M or ny >= N:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return 1

    count = 0
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count += bfs(i, j)
    print(count)


# DFS 풀이방법

# 재귀깊이 설정
sys.setrecursionlimit(10000)
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0] * (N) for _ in range(M)]
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y):
        if x < 0 or y < 0 or x >= M or y >= N or graph[x][y] == 0:
            return False
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    for i in range(K):
        a, b = map(int, input().split())
        graph[a][b] = 1

    for i in range(M):
        for j in range(N):
            if dfs(i, j):
                result += 1
    print(result)
