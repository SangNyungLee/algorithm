def dfs(start, arr):
    if start == m:
        answer.append(arr)
        return
    for j in range(1, n + 1):
        if not visited[j]:
            visited[j] = True
            dfs(start + 1, arr + [j])
            visited[j] = False


n, m = map(int, input().split())
answer = []
visited = [False] * (n + 1)

dfs(0, [])

for i in answer:
    print(*i)
