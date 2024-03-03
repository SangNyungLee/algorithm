from collections import deque


def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    cnt = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt


def solution(n, wires):
    answer = []
    for i in range(len(wires)):
        new_wires = [i for i in wires]
        graph = [[] for _ in range(n + 1)]
        new_wires.pop(i)
        result = []  # 결과값들 담을거임
        for a, b in new_wires:
            graph[a].append(b)
            graph[b].append(a)
        visited = [False] * (n + 1)
        for j in range(1, n + 1):
            if not visited[j]:
                if len(result) > 2:
                    break
                else:
                    result.append(bfs(graph, j, visited))
        answer.append(abs(result[0] - result[1]))
    return min(answer)
