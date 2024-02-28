import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    for _ in range(b):
        c, d = map(int, input().split())
    print(a - 1)
