import sys

input = sys.stdin.readline

n = int(input().rstrip())
count = 0
while True:
    if n % 5 != 0:
        n -= 3
        count += 1
    elif n % 5 == 0:
        count += n // 5
        print(count)
        break

    if n < 0:
        print(-1)
        break
