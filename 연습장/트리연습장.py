import sys
sys.setrecursionlimit(2500)
input = sys.stdin.readline

# 대각선도 움직임이 가능하다.
dx = [-1,-1,-1,1, 1,1, 0, 0]
dy = [0, 1, -1,-1, 1,0, -1, 1]


def dfs(x,y):
    if x < 0 or y < 0 or x >= h or y >= w or graph[x][y] == 0:
        return False
    
    visited[x][y] = True
    graph[x][y] = 0
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        dfs(nx,ny)
    return True

while True:
    w,h = map(int, input().split())
    island = 0 # 섬 개수 출력
    # w,h가 0이 되면 반복문 종료
    if w == 0 and h == 0:
        break
    graph = []
    
    # 좌표 추가
    for i in range(h):
        graph.append(list(map(int, input().split())))

    # 방문한 곳 표시
    visited = [[False] * (w) for _ in range(h)]
    result = 0
    # 그래프 하나씩 탐색하기
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                dfs(i,j)
                result += 1
    print(result)