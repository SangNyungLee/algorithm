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
