import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
start, end = map(int, input().split())
distance = [INF] * 100001


def djikstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        # -1, 1, 2인 경우
        for i in [-1, 1, 2]:
            if i == -1:
                next_pos = now - 1
                if 0 <= next_pos <= 100000 and dist + 1 < distance[next_pos]:
                    distance[next_pos] = dist + 1
                    heapq.heappush(queue, (dist + 1, next_pos))
            elif i == 1:
                next_pos = now + 1
                if next_pos <= 100000 and dist + 1 < distance[next_pos]:
                    distance[next_pos] = dist + 1
                    heapq.heappush(queue, (dist + 1, next_pos))
            elif i == 2:
                next_pos = now * 2
                if next_pos <= 100000 and dist < distance[next_pos]:
                    distance[next_pos] = dist
                    heapq.heappush(queue, (dist, next_pos))


djikstra(start)
print(distance[end])
