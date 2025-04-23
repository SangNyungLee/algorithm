from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False] * (n)
    
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, n, computers)
            answer += 1
    return answer

def bfs(idx, visited, n, graph):
    queue = deque()
    queue.append(idx)
    visited[idx] = True
    while queue:
        cur = queue.popleft()
        for i in range(n):
            if not visited[i] and graph[cur][i]:
                visited[i] = True
                queue.append(i)