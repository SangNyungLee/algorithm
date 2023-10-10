import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
dic={}
arr=[]
result = 0
for i in range(n):
    a = str(sys.stdin.readline().rstrip())
    dic[a] = 0
for i in range(m):
    a = str(sys.stdin.readline().rstrip())
    if a in dic:
        result += 1
        arr.append(a)
arr.sort()
print(result)
for i in arr:
    print(i)


