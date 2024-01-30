import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
dic = {i: 0 for i in arr2}

for i in arr:
    if i in dic:
        dic[i] += 1

for num in arr2:
    print(dic[num], end=" ")

#######이분탐색을 이용##########
import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
array2 = list(map(int, input().split()))
for i in range(M):
    target = array2[i]
    count = bisect_right(array, target) - bisect_left(array, target)
    print(count, end=" ")
