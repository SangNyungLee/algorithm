def solution(n, times):
    start = 1
    end = max(times) * n

    while start <= end:
        mid = (start + end) // 2
        exam = 0
        for time in times:
            exam += mid // time

        if exam >= n:
            end = mid - 1
        else:
            start = mid + 1
    return start
