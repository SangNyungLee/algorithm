import heapq, sys

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    heapq.heappush(arr, int(input()))
result = 0
while arr:
    if len(arr) == 1:
        break
    else:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        result += a + b
        heapq.heappush(arr, (a + b))
print(result)
