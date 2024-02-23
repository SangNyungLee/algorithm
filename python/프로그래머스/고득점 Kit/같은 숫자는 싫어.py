from collections import deque


def solution(arr):
    check = arr[0]
    answer = []
    answer.append(check)
    for i in range(1, len(arr)):
        if check == arr[i]:
            continue
        else:
            answer.append(arr[i])
            check = arr[i]

    return answer
