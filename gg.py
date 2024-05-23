<<<<<<< HEAD
=======
def dfs(n, lst):
    # 종료조건(n에 관련된) 처리 + 정답처리
    if n == M:  # M개의 수열을 완성
        ans.append(lst)
        return

    # 하부단계(함수) 호출
    for j in range(1, N + 1):
        if visited[j] == 0:  # 선택하지 않은 숫자인 경우 추가
            visited[j] = 1
            dfs(n + 1, lst + [j])
            visited[j] = 0


N, M = map(int, input().split())
ans = []  # 정답을 저장할 리스트
visited = [0] * (N + 1)  # 중복확인을 위한 visited 배열

dfs(0, [])

for lst in ans:
    print(*lst)
>>>>>>> 4b747d5b9f3836d7b8d1369cc97b14f8de0bbbe5
