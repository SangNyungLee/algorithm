n = int(input())
num = 0
if n < 100:
    print(n)
else:
    for i in range(100, n + 1):
        if i == 1000:
            continue
        check = [0, 0, 0]
        for a, b in enumerate(str(i)):
            check[a] = int(b)
        if (check[0] - check[1]) == (check[1] - check[2]):
            num += 1
    print(num + 99)
