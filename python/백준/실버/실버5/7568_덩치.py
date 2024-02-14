import sys

input = sys.stdin.readline

n = int(input().rstrip())
array = []
for _ in range(n):
    a, b = map(int, input().split())
    array.append((a, b))

for i in array:
    rank = 1
    for j in array:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
