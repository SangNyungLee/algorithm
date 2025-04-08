from collections import deque
"""
0 : 북
1 : 동
2 : 남
3 : 서
--
0 : 청소되지 않은 빈 칸
1 : 벽에 있는
2 : 청소가 완료된 칸
"""
N,M = map(int, input().split())
startX, startY, z = map(int, input().split())
arr = []
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#북 -> 서 -> 남 -> 동 : 반 시계 방향으로 움직이기

for _ in range(N):
    arr.append(list(map(int, input().split())))
# 마지막 좌표 값은 : (N-1, M-1)
answer = 0
def bfs(startX, startY, z):
    global answer
    queue = deque()
    queue.append((startX,startY, z))
    while queue:
        x,y,forward = queue.popleft() # z : 내가 바라보고 있는 방향
        flag = 1
        # 1. 현재 칸이 청소가 되어있나?
        if arr[x][y] == 0: # 청소 x -> 청소하기
            answer += 1
            arr[x][y] = 2
        if arr[x][y] == 2: # 청소 O -> 청소할거 찾기
            # flag = 0 # 만약에 4방향을 전부 봤는데 청소할게 없으면 돌아가야 됨
            for i in range(4): # 반시계 90도 회전하니까 1부터 
                new_forward = (forward + 3 - i) % 4 # 반시계 회전하는거 체크
                if new_forward > 3:
                    new_forward = 0
                nx = x + dx[new_forward]
                ny = y + dy[new_forward]
                if arr[nx][ny] == 1 or arr[nx][ny] == 2:
                    continue
                if arr[nx][ny] == 0:
                    flag = 0
                    queue.append((nx,ny,new_forward)) # 다음 좌표와 내가 바라보고 있는 방향 주기
                    break
        if flag: # 청소를 할게 없으면
            back = (forward + 2) % 4
            nx = x + dx[back]
            ny = y + dy[back]
            # 뒤로 갈 수 잇는지 확인하고 뒤로 못 가면 그대로 청소종료
            if arr[nx][ny] == 1:
                return
            queue.append((nx,ny,forward)) # 뒤로갈 때 방향은 그대로 냅두고 몸만 뒤로 가야됨
bfs(startX, startY, z)
print(answer)