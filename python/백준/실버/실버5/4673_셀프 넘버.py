check = [False] * (10001)


def dfs(n):
    check[n] = True
    if n < 10:
        n += n
        dfs(n)
    else:
        for i in str(n):
            n += int(i)
        if n > 10000:
            return
        dfs(n)


for i in range(1, 10001):
    if not check[i]:
        print(i)
        dfs(i)
