import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
true = [False] * (n + 1)
t = input().strip()
# 진실을 아는 사람 넣기
if t != "0":
    t = t.split()
    for i in range(1, len(t)):
        true[int(t[i])] = True

graph = []
for i in range(m):
    arr = list(map(int, input().split()))
    graph.append(arr[1::])

# 진실을 알고 있는 사람이랑 같이 있으면 진실로 바뀜
while True:
    change = 0
    for i in range(len(graph)):
        for j in graph[i]:
            if true[j] == True:
                for k in graph[i]:
                    true[k] = True
                graph[i] = []
                change += 1
                continue
    if change == 0:
        break
result = 0
for i in graph:
    if len(i) != 0:
        result += 1
print(result)
