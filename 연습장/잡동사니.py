import sys

input = sys.stdin.readline

k, n = map(int, input().split())
array = []
for i in range(k):
    array.append(int(input()))


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for i in array:
            qq = i // mid
            cnt += qq
        if cnt < target:
            end = mid - 1
        else:
            start = mid + 1
    print(end)


binary_search(array, n, 0, max(array))
