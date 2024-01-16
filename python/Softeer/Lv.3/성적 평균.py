import sys

input = sys.stdin.readline

N, K = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(K):
    a, b = map(int, input().split())
    num = sum(S[(a - 1) : b]) / (b - a + 1)
    print("%0.2f" % num)
