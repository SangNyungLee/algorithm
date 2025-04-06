import math

#시험장의 개수
n = int(input())
# 응시자의 수
room = list(map(int, input().split()))
# b : 총감독관 감시할 수 있는 응시자의 수
# c : 부감독관 감시할 수 있는 응시자의 수
b,c = map(int, input().split())
result = 0
for i in room:
    sum = 0
    if i <= b:
        sum += 1
    elif i > b:
        i -= b
        sum += 1
        if i % c != 0:
            sum += 1
        sum = sum + math.trunc(i / c)
    result += sum
print(result)