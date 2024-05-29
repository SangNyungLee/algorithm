def dfs(n, res, add, sub, mul, div):
    global mn, mx
    # 종료조건
    if n == N:
        mn = min(res, mn)
        mx = max(res, mx)
        return

    if add > 0:
        dfs(n + 1, res + lst[n], add - 1, sub, mul, div)
    if sub > 0:
        dfs(n + 1, res - lst[n], add, sub - 1, mul, div)
    if mul > 0:
        dfs(n + 1, res * lst[n], add, sub, mul - 1, div)
    if div > 0:
        dfs(n + 1, int(res / lst[n]), add, sub, mul, div - 1)


N = int(input())
lst = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
mn, mx = int(1e9), int(-1e9)
dfs(1, lst[0], add, sub, mul, div)
print(mx)
print(mn)
