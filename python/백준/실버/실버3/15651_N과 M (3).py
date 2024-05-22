def dfs(start, s, arr):
    if start == m:
        answer.append(arr)
        return
    for j in range(s, n + 1):
        dfs(start + 1, j, arr + [j])


n, m = map(int, input().split())
answer = []
visited = [False] * (n + 1)

dfs(0, 1, [])
for i in answer:
    print(*i)
