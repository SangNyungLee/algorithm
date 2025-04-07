n = int(input())
t = [0]
p = [0]
for _ in range(n):
    a,b = map(int, input().split())
    t.append(a)
    p.append(b)
dp = [[] for _ in range(n + 1)] # n일 까지 셀거임 
dp2 = [[0] for _ in range(n + 1)] # 최대값 넣는 리스트

for i in range(1, len(t)):
    num = t[i] + (i - 1) # 돈 받는 날짜 (x, [y]) x일에 y일에 일한걸 받을 수 있음
    if num > n:
        continue
    dp[num].append(i)

for i in range(1, len(dp)):
    if dp[i]:
        check = []
        for j in dp[i]:
            print("i", i, "j",j, end=" ")
            check.append(p[j] + dp2[j][0]) ## dp2[j] -> dp2[j-1]
            print("check :", p[j],"+",dp2[j][0])
        maxNum = max(check)
        dp2[i][0] = maxNum ## maxNum,dp2[i-1] 비교로 변경
    else:
        dp2[i] = dp2[i-1]

print("dp :", end=" ")
for i in range(1, len(dp)):
    print(dp[i], end=" ")
print()
print("dp2:", end=" ")
for i in range(1, len(dp2)):
    print(dp2[i], end=" ")