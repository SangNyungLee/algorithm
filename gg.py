# import heapq
# import sys

# input = sys.stdin.readline
# n = int(input())
# queue = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     heapq.heappush(queue, (a, b))
# a, b = max(queue)
# room = []
# start, end = heapq.heappop(queue)
# room.append([end])
# while queue:
#     start, end = heapq.heappop(queue)
#     flag = False
#     for i in room:
#         if i[0] <= start:
#             i[0] = end
#             flag = True
#             break
#     if not flag:
#         room.append([end])
# print(len(room))

import heapq, sys

input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(queue, (a, b))
room = []
start, end = heapq.heappop(queue)
heapq.heappush(room, end)
while queue:
    start, end = heapq.heappop(queue)
    if room[0] <= start:
        heapq.heappop(room)
        heapq.heappush(room, end)
    else:
        heapq.heappush(room, end)
print(len(room))
