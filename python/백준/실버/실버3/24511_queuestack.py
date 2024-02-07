import sys
from collections import deque

input = sys.stdin.readline
n = int(input().rstrip())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
m = int(input().rstrip())
C = list(map(int, input().split()))
result = deque()
# for i in range(m):
#     move = C[i]
#     for j in range(n):
#         if A[j] == 0:  # 큐일 경우(기존거 빼기)
#             t = B[j]
#             B[j] = move
#             move = t
#         else:  # 스택일 경우(새로 들어온애 빼기)
#             continue
#     print(move, end=" ")

for i in range(n):
    if A[i] == 0:
        result.append(B[i])
for i in C:
    result.appendleft(i)
for i in range(m):
    print(result.pop(), end=" ")
