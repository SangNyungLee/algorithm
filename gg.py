# n = int(input())
# alpha = []
# alpha_check = {}
# dic = {}
# arr = []
# for _ in range(n):
#     tt = str(input())
#     arr.append(list(tt))
# MAX = 0
# # 배열 중에서 가장 큰 값 뽑기
# for i in arr:
#     MAX = max(MAX, len(i))
# # 비어있는 곳은 0으로 채워서 자릿수 맞춰줌
# for i in range(len(arr)):
#     if len(arr[i]) < MAX:
#         check = MAX - len(arr[i])
#         for j in range(check):
#             arr[i].insert(0, "0")
# # 높은 숫자부터 차례대로 출력하기
# num = 9
# for i in range(MAX):
#     for j in range(len(arr)):
#         # 값이 있으면 딕셔너리에 넣어버림
#         if arr[j][i] != "0" and arr[j][i] not in alpha:
#             alpha.append(arr[j][i])
#             dic[arr[j][i]] = str(num)
#             arr[j][i] = str(num)
#             num-=1
#         if arr[j][i] in alpha:
#             arr[j][i] = dic[arr[j][i]]
# result = 0
# for i in range(len(arr)):
#     result +=int("".join(arr[i]))
# print(dic)
# print(result)

n = int(input())
dic = {}
arr = []
for _ in range(n):
    tt = str(input())
    arr.append(list(tt))

for i in arr:
    cnt = len(i)
    for j in i:
        if j not in dic:
            dic[j] = (10**(cnt-1))
        else:
            dic[j] += (10**(cnt-1))
        cnt -=1

d2 = list(dic.values())
d2.sort(reverse=True)
num = 9
result = 0
for i in d2:
    result += i*num
    num -= 1
print(result)