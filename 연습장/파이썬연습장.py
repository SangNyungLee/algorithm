import sys;
import math;
# n = int(sys.stdin.readline().rstrip())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# arr2 = list(map(int, sys.stdin.readline().rstrip().split()))

dic ={i: 0 for i in range(0, 246913)}
for i in dic:
    num = i
    newA = int(math.sqrt(num))
    cnt = 0
    for i in range(2, newA+1):
        if num%i == 0:
            cnt += 1
            break
    if(cnt == 0 and i != 1):
        dic[num] = 1
    if(num > 1):
        dic[num] = dic[num]+dic[num-1]
while True:
    a = int(input())
    if a == 0:
        break
    else:
        print(dic[a*2] - dic[a])