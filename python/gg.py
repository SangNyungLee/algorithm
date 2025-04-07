
n = int(input())
t = [0]
p = [0]
dp = [[] for _ in range(n + 1)]
dp2 = [0] * (n + 1)

for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)

for i in range(1, n + 1):
    num = t[i] + (i - 1)
    if num > n:
        continue
    dp[num].append(i)

for i in range(len(dp)):
    if dp[i]:
        check = []
        for j in dp[i]:
            check.append(dp2[j - 1] + p[j])
        maxNum = max(check)
        dp2[i] = max(maxNum, dp2[i-1])  
    else:
        dp2[i] = max(dp2[i], dp2[i - 1])

print("------------")
print("t", t)
print("p",p)
print("dp",dp)
print("dp2",dp2)