import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
result = []
for _ in range(n):
    a = str(input())
    graph.append([i for i in a])


def check(x, y):
    count = 0
    for i in range(x, x + 8):
        if i % 2 == 0:
            color = "B"
        else:
            color = "W"
        for j in range(y, y + 8):
            if graph[i][j] != color:
                count += 1
            if color == "W":
                color = "B"
            else:
                color = "W"
    count2 = 0
    for i in range(x, x + 8):
        if i % 2 == 0:
            color = "W"
        else:
            color = "B"
        for j in range(y, y + 8):
            if graph[i][j] != color:
                count2 += 1
            if color == "W":
                color = "B"
            else:
                color = "W"
    return min(count, count2)


for i in range(n - 7):
    for j in range(m - 7):
        result.append(check(i, j))
print(min(result))
