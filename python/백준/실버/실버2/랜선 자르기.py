import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for i in range(K):
    arr.append(int(input()))

start = 1
end = max(arr)

while start <= end:
    count = 0
    mid = (start + end) // 2

    for x in arr:
        count += x // mid

    if count < N:
        end = mid - 1
    else:
        start = mid + 1
print(end)
