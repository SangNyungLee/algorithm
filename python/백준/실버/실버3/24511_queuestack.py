import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input().rstrip())
C = list(map(int, input().split()))
queue = deque()

for i in range(n):
    if A[i] == 0:
        queue.append(B[i])
for i in C:
    queue.appendleft(i)
for i in range(m):
    print(queue.pop(), end=" ")
