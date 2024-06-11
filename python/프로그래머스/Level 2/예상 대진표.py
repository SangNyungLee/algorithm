import math


def solution(n, a, b):
    answer = 0
    while True:
        print(a, b)
        if abs(a - b) == 1 and max(a, b) % 2 == 0:
            return answer + 1
        if a == 1:
            b = math.ceil(b / 2)
        elif b == 1:
            a = math.ceil(a / 2)
        else:
            a = math.ceil(a / 2)
            b = math.ceil(b / 2)
        answer += 1
    return answer
