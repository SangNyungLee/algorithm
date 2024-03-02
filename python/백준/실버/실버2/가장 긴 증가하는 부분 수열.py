import sys

sys.setrecursionlimit(10**9)
n = int(input())
arr = list(map(int, input().split()))
result = []


# 재귀 함수로 구현
def recursion(idx):
    leng = 1
    check = arr[idx]
    for i in range(idx, len(arr) - 1):
        if check < arr[i + 1]:
            check = arr[i + 1]
            leng += 1
        else:
            recursion(i + 1)
    return result.append(leng)


recursion(0)
print(max(result))
