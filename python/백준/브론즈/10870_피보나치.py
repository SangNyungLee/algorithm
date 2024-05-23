n = int(input())


def fivo(n):
    if n <= 1:
        return 1
    else:
        return fivo(n - 1) + fivo(n - 2)


print(fivo(n))
