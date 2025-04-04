x = 3
y = 5

graph = [[0] * (x) for _ in range(y)]
count = 0
for i in range(y):
    for j in range(x):
        count += 1
        graph[i][j] = count
print(graph)