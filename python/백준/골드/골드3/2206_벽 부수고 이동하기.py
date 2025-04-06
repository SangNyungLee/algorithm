from collections import deque
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# visited =[[[0] * 2] * (m) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
# visited[x][y][0] -> 벽을 안 부순 경로
# visited[x][y][1] -> 벽을 한 번 부순 경로
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 일단 그냥 원래대로 돌아다님
# 벽을 한 번도 안 부쉈을 때 그 벽을 부수고 1로 색칠함
# 1인데 이미 벽을 한 번더 만나면 그대로 종료

def bfs():
    queue = deque()
    queue.append((0,0,0)) # x,y,벽 부쉈는지 체크
    visited[0][0][0] = 1
    while queue:
        x,y,skill = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 못 가는 길은 통과
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 이미 방문했으면 갈 필요 없음(무조건 그 전에 방문한 애가 더 빠름)
            if visited[nx][ny][skill] != 0:
                continue
            # 이미 벽을 부수고 왔는데 다음 길에 또 벽이 있으면 통과
            if skill == 1 and graph[nx][ny] == 1:
                continue
            # 이미 벽 부쉈는데 다음 길이 벽이 아닐 때
            if skill == 1 and graph[nx][ny] == 0:
                visited[nx][ny][1] = visited[x][y][1] + 1
                queue.append((nx,ny,1))
            
            # 벽을 아직 안 부쉈는데 벽을 만났을 때
            if skill == 0 and graph[nx][ny] == 1:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx,ny,1))

            # 벽을 아직 안 부쉈는데 또 벽이 아닐 때
            if skill == 0 and graph[nx][ny] == 0:
                visited[nx][ny][0] = visited[x][y][0] + 1
                queue.append((nx,ny,0))
bfs()

# 둘다 0이면 도달하지 못함
if visited[n-1][m-1][0] == 0 and visited[n-1][m-1][1] == 0:
    print(-1)
# 둘중 하나만 0이면 나머지는 도달한거임
elif visited[n-1][m-1][0] == 0 or visited[n-1][m-1][1] == 0:
    print(max(visited[n-1][m-1][0],visited[n-1][m-1][1]))
# 둘다 도달했다면 더 작은 값을 출력
else:
    print(min(visited[n-1][m-1][0],visited[n-1][m-1][1]))