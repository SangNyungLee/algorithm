N, S = map(int, input().split())
arr = list(map(int, input().split()))
answer = 0


def dfs(n, res):
    global answer
    if n == N:
        return

    res += arr[n]

    if res == S:
        answer += 1
    dfs(n + 1, res)
    dfs(n + 1, res - arr[n])


dfs(0, 0)
print(answer)

# def subsets(arr):
#     global result

#     def backtrack(start, subset):
#         result.append(subset[:])
#         for i in range(start, len(arr)):
#             subset.append(arr[i])
#             backtrack(i + 1, subset)
#             subset.pop()

#     backtrack(0, [])
#     return result


# subsets(arr)
# answer = 0
# for i in result:
#     if sum(i) == S and len(i) > 0:
#         answer += 1

# print(answer)
