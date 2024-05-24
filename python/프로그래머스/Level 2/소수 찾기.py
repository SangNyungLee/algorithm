from itertools import permutations


def solution(numbers):
    nums = [i for i in numbers]
    arr = []
    for i in range(1, len(nums) + 1):
        arr += list(permutations(nums, i))
    new_arr = [int("".join(p)) for p in arr]
    new_arr = set(new_arr)
    prime_arr = [True] * (max(new_arr) + 1)
    prime_arr[0] = False
    prime_arr[1] = False
    result = []
    count = 0
    for i in range(2, len(prime_arr)):
        if prime_arr[i]:
            result.append(i)
            for j in range(2 * i, len(prime_arr), i):
                prime_arr[j] = False
    for k in new_arr:
        if k in result:
            count += 1
    return count
