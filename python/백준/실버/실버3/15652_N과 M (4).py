def dfs(start, arr):
    if start == m:
        arr.sort()
        if arr not in answer:
            answer.append(arr)
        return
    for j in range(1, n + 1):
        dfs(start + 1, arr + [j])


n, m = map(int, input().split())
answer = []
visited = [False] * (n + 1)

dfs(0, [])
for i in answer:
    print(*i)
