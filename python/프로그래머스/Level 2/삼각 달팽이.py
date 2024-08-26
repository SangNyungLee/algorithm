def solution(n):
    answer = []
    total_length = (n * (n + 1)) // 2
    graph = [[0] * i for i in range(1, n + 1)]  # 숫자 하나씩 넣을 그래프
    visited = [[False] * i for i in range(1, n + 1)]  # 방문표시
    move = 0  # down : 0, right : 1, up : 2 순서로 움직일거임
    x = 0  # 움직일 좌표임
    y = 0
    for i in range(1, total_length + 1):
        graph[x][y] = i
        visited[x][y] = True
        if i == total_length:
            break
        if move == 0:  # down
            if ((x + 1) < n) and not visited[x + 1][y]:  # 방문할 수 있는 곳이면
                x += 1
            else:  # 방문했거나 x + 1 > n이면
                y += 1
                move = 1

        elif move == 1:  # 오른쪽으로 움직이는 경우
            if ((y + 1) < n) and not visited[x][y + 1]:
                y += 1
            else:  # 위로 올라가는 경우
                x -= 1
                y -= 1
                move = 2
        else:
            if ((x - 1) > 0 and (y - 1) > 0) and not visited[x - 1][y - 1]:
                x -= 1
                y -= 1
            else:
                x += 1
                move = 0
    for i in graph:
        for j in i:
            answer.append(j)
    return answer
