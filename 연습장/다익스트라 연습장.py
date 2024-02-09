import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

print(graph)
