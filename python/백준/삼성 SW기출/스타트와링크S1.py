N = int(input())
M = N // 2
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
MIN = int(1e9)


def dfs(n, alst, blst):
    global MIN
    if n == N:
        asum = 0
        bsum = 0
        if len(alst) == len(blst):
            for i in range(M):
                for j in range(M):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            MIN = min(MIN, abs(asum - bsum))
        return
    dfs(n + 1, alst + [n], blst)
    dfs(n + 1, alst, blst + [n])


dfs(0, [], [])
print(MIN)
                