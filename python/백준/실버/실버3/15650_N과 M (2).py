def dfs(n, s, lst):
    if n == M:
        answer.append(lst)
        return
    for j in range(s, N + 1):
        dfs(n + 1, j + 1, lst + [j])


N, M = map(int, input().split())
answer = []
dfs(0, 1, [])
for i in answer:
    print(*i)
