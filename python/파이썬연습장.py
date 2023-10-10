import sys

# n = int(sys.stdin.readline().rstrip())
# arr = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
n = 10
arr = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
m = 8
arr2 = [10, 9, -5, 2, 3, 4, 5, -10]
dic = {i: 0 for i in arr2}
for i in arr:
    if i in dic:
        dic[i] += 1

for num in arr2:
    print(dic[num], end=" ")
