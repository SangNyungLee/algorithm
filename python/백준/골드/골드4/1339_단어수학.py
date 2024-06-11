n = int(input())
dic = {}
arr = []
for _ in range(n):
    tt = str(input())
    arr.append(list(tt))

for i in arr:
    cnt = len(i)
    for j in i:
        if j not in dic:
            dic[j] = (10**(cnt-1))
        else:
            dic[j] += (10**(cnt-1))
        cnt -=1

d2 = list(dic.values())
d2.sort(reverse=True)
num = 9
result = 0
for i in d2:
    result += i*num
    num -= 1
print(result)