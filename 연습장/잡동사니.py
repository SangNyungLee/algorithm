import sys

input = sys.stdin.readline

n = int(input().rstrip())
count = n // 5
n = n % 5
count = count + (n // 3)
if n % 3 == 0:
    print(count)
else:
    print(-1)
