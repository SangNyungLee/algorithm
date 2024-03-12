arr = []
n = len(arr)
answer = [0, 0]


def press(start, end, n):
    temp = arr[start][end]
    for i in range(start, start + n):
        for j in range(end, end + n):
            if temp != arr[i][j]:
                n //= 2
                press(start, end, n)
                press(start, end + n, n)
                press(start + n, end, n)


press(0, 0, n)
