import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(idx):
    for i in graph[idx]: # 연결된 노드에만 방문해야 해야됨
        if not parent[i]:
            parent[i] = idx # 방문하고 자식 노드를 불러낼 때 저장해놓음
            dfs(i)
n = int(input())
graph= [[] for _ in range(n + 1)]
parent = [0] * (n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
for i in parent[2:]:
    print(i)