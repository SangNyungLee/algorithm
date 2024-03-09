k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))

arr.sort()
start = 0
end = max(arr)


while start <= end:
    count = 0
    mid = (start + end) // 2
    for i in arr:
        count += i // mid
    if count < n:
        end = mid - 1
    else:
        start = mid + 1

print("end", end)
print("start", start)
