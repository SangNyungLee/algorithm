import sys

n = int(sys.stdin.readline().rstrip())
dp = []
for i in range(n):
    dp.append(list(map(int, sys.stdin.readline().rstrip().split())))

for i in range(1, n):
    dp[i][0] = min(dp[i][0] + dp[i - 1][1], dp[i][0] + dp[i - 1][2])
    dp[i][1] = min(dp[i][1] + dp[i - 1][0], dp[i][1] + dp[i - 1][2])
    dp[i][2] = min(dp[i][2] + dp[i - 1][0], dp[i][2] + dp[i - 1][1])

print(min(dp[-1]))
