import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break


def post(start, end):
    if start > end:
        return
    # 종료지점 설정
    mid = end + 1
    # mid 찾기
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            mid = i
            break

    # 왼쪽 탐색
    post(start + 1, mid - 1)
    post(mid, end)
    print(arr[start])


post(0, len(arr) - 1)
