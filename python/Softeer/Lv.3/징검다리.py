n = 15
stones = [5, 3, 9, 4, 8, 2, 6, 7, 1, 10, 11, 12, 13, 14, 15]
dp = [1] * n

for i in range(1, n):
    find = 0
    for j in range(i):
        if stones[j] < stones[i]:
            find = max(find, dp[j])
    dp[i] = find + 1

print(max(dp))
