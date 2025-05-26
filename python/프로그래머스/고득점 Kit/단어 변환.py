from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    graph = [[False] * n for _ in range(n)]
    answer = []

    # 1. 단어 간 변환 가능 여부로 그래프 만들기
    for i in range(n):
        for j in range(i + 1, n):
            diff = sum(1 for a, b in zip(words[i], words[j]) if a != b)
            if diff == 1:
                graph[i][j] = graph[j][i] = True

    # 2. begin에서 변환 가능한 단어들을 찾아 BFS 실행
    for i in range(n):
        diff = sum(1 for a, b in zip(begin, words[i]) if a != b)
        if diff == 1:
            answer.append(bfs(i, n, graph, words, target))

    # 3. 도달한 것들만 필터링해서 최솟값 반환
    valid = [x for x in answer if x < 1_000_000]
    return min(valid) if valid else 0

def bfs(start_idx, n, graph, words, target):
    queue = deque()
    visited = [False] * n
    queue.append((start_idx, 1))
    visited[start_idx] = True

    while queue:
        cur, cnt = queue.popleft()
        if words[cur] == target:
            return cnt
        for next_idx in range(n):
            if not visited[next_idx] and graph[cur][next_idx]:
                visited[next_idx] = True
                queue.append((next_idx, cnt + 1))

    return 1_000_000  # target에 도달하지 못한 경우
