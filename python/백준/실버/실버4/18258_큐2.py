from collections import deque
import sys

a = int(sys.stdin.readline().rstrip())
queue = deque()
for i in range(a):
    t = str(sys.stdin.readline().rstrip())
    if "push" in t:
        newNum = t.replace("push", "")
        queue.append(int(newNum))
    elif "pop" in t:
        if queue:
            print(queue.popleft())
        else:
            print("-1")
    elif "size" in t:
        print(len(queue))
    elif "empty" in t:
        if queue:
            print("0")
        else:
            print("1")
    elif "front" in t:
        if queue:
            print(queue[0])
        else:
            print("-1")
    else:
        if queue:
            print(queue[-1])
        else:
            print("-1")
