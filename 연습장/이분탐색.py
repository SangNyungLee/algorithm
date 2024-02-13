import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
arr.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


start = 0
end = len(arr)
for target in arr2:
    # result = binary_search(arr, target, 0, len(arr) - 1)
    # if result == None:
    #     print(0)
    # else:
    #     print(1)
    count = bisect_right(arr, target) - bisect_left(arr, target)
    if count != 0:
        print(1)
    else:
        print(0)
