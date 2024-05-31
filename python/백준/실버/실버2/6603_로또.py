# from itertools import combinations

# while True:
#     arr = list(map(int, input().split()))
#     k = arr[0]
#     s = arr[1:]

#     for i in combinations(s, 6):
#         print(*i)
#     if k == 0:
#         break
#     print()

arr = [7, 1, 2, 3, 4, 5, 6, 7]
arr2 = arr[1:]
result = []


def dfs(n, idx):
    if n == 6:
        print(result)
        return

    for i in range(idx, arr[0]):
        result.append(arr2[i])
        dfs(idx + 1, i + 1)
        result.pop()


dfs(0, 0)
