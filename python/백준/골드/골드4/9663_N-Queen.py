N = int(input())
v1 = [False] * N  # 열 체크
v2 = [False] * (N * 2)  # i+j 대각선 체크
v3 = [False] * (N * 2)  # i-j 대각선 체크
answer = 0  # 경우의 수를 담을 변수


def dfs(n):
    global answer
    # 종료조건
    if n == N:
        answer += 1
        return
    for j in range(N):
        if not v1[j] and not v2[n + j] and not v3[n - j]:
            v1[j] = v2[n + j] = v3[n - j] = True
            dfs(n + 1)
            v1[j] = v2[n + j] = v3[n - j] = False


dfs(0)  # 인덱스가 0부터 시작하니깐 1이 아니라 0임
print(answer)
