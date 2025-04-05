from collections import deque

# m : 가로, n : 세로
m,n = map(int, input().split())

tomato = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
    tomato.append(list(map(int, input().split())))

# 1 : 익은 토마토
# 0 : 익지 않은 토마토
# -1 : 토마토가 없는 칸
# 토마토가 하나 이상 있는 경우만 입력으로 주어짐
# 저장 될 때부터 모든 토마토가 익어있는 상태면 0을 출력해야됨
# 토마토가 모두 익지 못하는 상황이면 -1 출력

queue = deque()
for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            queue.append((x, y, 0)) # (x, y, 익은 날짜 순서)
date = 0
while queue:
    x,y,z = queue.popleft()
    if z > date:
        date = z
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = 1
            queue.append((nx, ny, z + 1))

for x in range(n):
    for y in range(m):
        if tomato[x][y] == 0:
            # 토마토가 하나라도 안 익은게 있으면 -1
            date = -1
print(date)