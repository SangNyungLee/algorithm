n, k = list(map(int, input().split()))
queue = []
result = []
move = 0
for i in range(1, n + 1):
    queue.append(i)

# k 만큼씩 이동한다.
for i in range(1, n + 1):
    move += k - 1
    if move <= len(queue):
        result.append(queue.pop(move))
    else:
        move = move % len(queue)
        result.append(queue.pop(move))
print("<", end="")
for i in result:
    if result[-1] == i:
        print(i, end="")
    else:
        print(i, end=", ")
print(">", end="")
