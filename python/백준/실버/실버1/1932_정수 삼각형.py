import sys

dp = []
result = 0
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))
if i == 1:
    print(i)
else:
    dp[1][0] = dp[1][0] + dp[0][0]
    dp[1][1] = dp[1][1] + dp[0][0]

    for i in range(2, n):
        for j, value in enumerate(dp[i]):
            if j == 0:
                dp[i][0] = dp[i][0] + dp[i - 1][0]
            elif i == j:
                dp[i][j] = dp[i][j] + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]
    print(max(dp[-1]))
