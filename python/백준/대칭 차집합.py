import sys

n,m = map(int, sys.stdin.readline().rstrip().split())
dic1 ={}
dic2 ={}
result =0
arr1 = list(map(int, sys.stdin.readline().rstrip().split()))
arr2 = list(map(int, sys.stdin.readline().rstrip().split()))
for i in arr1:
    dic1[i] = 0
for i in arr2:
    dic2[i] = 0

for i in dic1.keys():
    if i not in dic2:
        result +=1
for i in dic2:
    if i not in dic1:
        result +=1
print(result)    
 
