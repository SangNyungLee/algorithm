import sys

input = sys.stdin.readline

n = int(input().rstrip())
x = []
y = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

print((max(x) - min(x)) * (max(y) - min(y)))
