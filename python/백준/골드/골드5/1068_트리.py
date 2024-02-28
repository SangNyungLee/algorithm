import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
graph = [[] for _ in range(N)]
visited = [False] * (N)
for i in range(N):
    if arr[i] == -1:
        continue
    else:
        graph[arr[i]].append(i)
# M값 지워버리기
for i in graph:
    if M in i:
        i.remove(M)
# 루트노드 저장 (무조건 0부터 시작하는거 아님)
rootNode = arr.index(-1)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True
    result = 0
    while queue:
        x = queue.popleft()
        if graph[x]:
            for i in graph[x]:
                if not visited[i]:
                    visited[i] = True
                    queue.append(i)
        else:
            result += 1
    return result


if rootNode == M:
    print(0)
else:
    print(bfs(rootNode))
