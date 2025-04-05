from collections import deque

m,n,h = map(int, input().split())
graph = [[] for _ in range(h)]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0 ,0]
dz = [0, 0, 0, 0, -1, 1]

for i in range(h):
    for _ in range(n):
        graph[i].append(list(map(int, input().split())))

position = deque()
 # 토마토의 좌표 찾기
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                position.append((z,x,y,0))
maxdate = 0     
while position:
    z,x,y,date = position.popleft()
    if maxdate < date:
        maxdate = date
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or ny < 0 or nz < 0 or nx >= n or ny >= m or nz >= h:
            continue
        if graph[nz][nx][ny] == 0:
            graph[nz][nx][ny] = 1
            position.append((nz,nx,ny, date + 1))

# 검사하기
flag = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 0:
                flag = 1
                break
if flag:
    print(-1)
else:
    print(maxdate)
                