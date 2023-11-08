import math
import sys

t = int(sys.stdin.readline().rstrip())
for i in range(t):
    k, n = list(map(int, sys.stdin.readline().rstrip().split()))
    result = 1
    result2 = 1
    for i in range(n, n - k, -1):
        result *= i
    for i in range(k, 1, -1):
        result2 *= i
    print(result // result2)
