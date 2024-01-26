import sys

input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

arr.sort(reverse=True)
MAX = 0  # 최대 중량 재는거
for i in range(n, 0, -1):
    w = i * arr[i - 1]
    if w > MAX:
        arr.pop()
        MAX = w
print(MAX)
