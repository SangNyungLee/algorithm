# k : 이미 가지고 있는 랜선의 개수
# n : 필요한 랜선의 개수
k, n = map(int, input().split())
arr = []
for i in range(k):
    arr.append(int(input()))
start = 0
end = max(arr)

while start <= end:
    mid = (start + end) // 2
    print("start", start, "end", end, "mid", mid)
    # 중앙값에 맞춰서 자르기
    count = 0
    for i in arr:
        count += i // mid

    if count < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)
