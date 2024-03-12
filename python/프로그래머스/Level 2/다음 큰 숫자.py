def solution(n):
    answer = 0
    num = len("".join(bin(n)[2:].split("0")))
    while True:
        n += 1
        check = len("".join(bin(n)[2:].split("0")))
        if check == num:
            break
    return n
