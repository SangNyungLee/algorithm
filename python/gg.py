from collections import deque

N, M = map(int, input().split()) # 마을의 크기, 용사의 좌표
S1, S2, E1, E2 = map(int, input().split()) # 메두사의 좌표, 공원의 좌표
mlst = list(map(int, input().split())) 
graph = []
visited = [[0] * N for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
parent = {}
path = deque()
# 제일먼저 할 것은 시작점부터 끝 점까지 출발할건데 최단 경로만 일단 구하기
# 1 : 벽, 0 : 길
def bfs():  
    queue = deque()
    queue.append((S1, S2))
    visited[S1][S2] = 1
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                parent[(nx, ny)] = (x,y)
                queue.append((nx,ny))

# 경로 역추적하는 함수
def find_parent():
    queue = deque()
    queue.append((E1, E2))
    while queue:
        x, y = queue.popleft()
        if (x, y) == (S1, S2):
            return
        xx, yy = parent[x,y]
        path.appendleft((xx,yy))
        queue.append((xx,yy))

# 내 위치를 기준으로 4방향으로 medusa의 vision을 설정하는 함수
def medusa_vision():
    x,y = path.popleft()
    print(x,y)
    queue = []

bfs()
if visited[E1][E2] == 0:
    print(-1)
    exit()
for i in visited:
    print(i)
print("공원 좌표", visited[E1][E2])
find_parent()
path.append((E1, E2))
print(path)
