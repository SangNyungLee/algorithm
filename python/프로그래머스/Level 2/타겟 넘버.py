answer = 0


def solution(numbers, target):
    def dfs(n, target, target_num):
        global answer
        if n == len(numbers):
            if target_num == target:
                answer += 1
            return
        dfs(n + 1, target, target_num + numbers[n])
        dfs(n + 1, target, target_num - numbers[n])

    dfs(0, target, 0)
    return answer
