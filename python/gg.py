from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    n = len(words) # words 배열의 길이
    arr = [False] * n
    graph = [[False] * n for _ in range(n)]
    answer = []
    for i in range(n):
        for j in range(i +1, n):
            diff = 0
            for x,y in zip(words[i], words[j]):
                if x != y:
                    diff += 1
            if diff == 1:
                graph[i][j] = True
                graph[j][i] = True
    for i in range(n):
        diff = 0
        for x, y in zip(begin, words[i]):
            if x != y:
                diff += 1
        if diff == 1:
            arr[i] = True
    for i in range(n):
        if arr[i] == True:
            answer.append(bfs(i, n, graph, words, target))

    valid = [x for x in answer if x < 1_000_000]
    return min(valid) if valid else 0

def bfs(idx, n, graph, words, target):
    queue = deque()
    visited = [False] * n
    queue.append((idx, 1))
    while queue:
        cur, ans = queue.popleft()
        if words[ans] == target:
            return ans
        for i in range(n):
            if not visited[i] and graph[i][cur]:
                queue.append((i, ans + 1))
                if words[i] == target:
                    return ans + 1
                visited[i] = True
    return 1_000_000