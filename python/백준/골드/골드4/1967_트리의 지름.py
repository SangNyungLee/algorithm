################# 다익스트라 알고리즘 풀이 ####################
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

if n == 1:
    print(0)
else:
    distance = [INF] * (n + 1)
    dijkstra(1)
    distance[0] = 0
    idx = distance.index(max(distance))
    distance = [INF] * (n + 1)
    dijkstra(idx)
    distance[0] = 0
    print(max(distance))

################ BFS 풀이 ################
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 0
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visited[i[0]] == -1:
                queue.append(i[0])
                visited[i[0]] = visited[x] + i[1]
                
visited = [-1] * (n+1)
bfs(1)
idx = visited.index(max(visited))
visited = [-1] * (n+1)
bfs(idx)
print(max(visited))