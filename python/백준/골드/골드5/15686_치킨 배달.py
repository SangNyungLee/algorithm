import itertools

N, M = map(int, input().split())
arr = []
INF = int(1e9)
for _ in range(N):
    arr.append(list(map(int, input().split())))
chicken = []
house = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        if arr[i][j] == 2:
            chicken.append((i, j))
pp = []
chicken_dist = [[] for _ in range(len(chicken))]
for a, b in house:
    for j in range(len(chicken)):
        c, d = chicken[j]
        dist = abs(a - c) + abs(b - d)
        chicken_dist[j].append(dist)
chicken_dist = itertools.combinations(chicken_dist, M)
for i in chicken_dist:
    answer = [INF] * len(house)
    for j in range(len(i[0])):  # 6개
        chk = []
        for k in range(len(i)):  # 2개
            chk.append(i[k][j])
        answer[j] = min(answer[j], min(chk))
    pp.append(sum(answer))
print(min(pp))
