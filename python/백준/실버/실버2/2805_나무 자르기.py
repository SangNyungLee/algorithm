import sys

input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array)

while start <= end:
    count = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            count += x - mid

    if count < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)
