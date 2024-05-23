# n, k = map(int, input().split())
# arr = list(map(int, input().split()))
# case = []
# # 조합 만들기
# for i in range(n):
#     for j in range(n):
#         case.append((arr[i],arr[j]))
# arr2 = sorted(case, key=lambda x:(x[0],x[1]))
# print(arr2)

n = int(input())
arr1 = list(map(int, input().split())) # 모자를 쓰고 싶은 사람
arr2 = list(map(int, input().split())) # 모자의 개수
visited = [False] * len(arr2)
arr1.sort()
arr2.sort()
count = 0

for i in range(n):
    for j in range(n):
        if arr2[j] <= arr1[i] + 3 and arr2[i] >= arr1[i] -3 and not visited[j]:
            visited[j] = True
            count += 1
            break
        if arr2[j] > arr1[i] + 3:
            break
print(visited)
print(count)

# N 명의 사람이 각각 원하는 모자 크기를 적었다. 

# 또, N개의 모자가 있고 크기들을 알고 있다.

# 원하는 모자 크기와 차이가 3 이하이면 모자를 쓸 수 있다. 최대 몇 명이 모자를 쓸 수 있게 되는가? 한 모자는 한 명만 쓸 수 있다.

 

# 아래와 같이 각 사람이 원하는 모자의 크기가 있다고 하자

# 4 8 2



# 아래는 N개의 모자의 크기이다

# 6 10 7



# 첫번째 사람이 원하는 모자의 크기는 4이고, 사이즈 6 또는 사이즈 7 모자를 쓸 수 있다

# 두번째 사람이 원하는 모자의 크기는 8이고, 사이즈 6, 사이즈 7, 사이즈 10 모자를 쓸 수 있다

# 세번째 사람이 원하는 모자의 크기는 2이고, 만족하는 모자는 존재하지 않는다



# 따라서, 위 내용을 조합해보면 첫번째 사람과 두번째 사람은 모자를 쓸 수 있고 답은 2가 된다



# [제약사항]

# 1.     N은 3 이상 500 이하이다. (3 ≤ N ≤ 500)

# 2.     원하는 모자의 크기와 실제 모자 크기들은 모두 1 이상 2,000 이하의 정수이다.

 

# [입력]

# 가장 첫 줄에는 테스트 케이스의 총 수가 주어진다.

# 그 다음 줄부터 각 테스트 케이스가 주어지며,

# 각 테스트 케이스는 3줄로 구성된다.

# 각 테스트 케이스의 첫 줄에는 N의 값이 주어진다.

# 다음 줄에 사람들이 원하는 모자의 크기들이 주어진다. 다음 줄에 실제 모자의 크기들이 주어진다.

 

# [출력]

# 출력의 각 줄은 ‘#x’로 시작하고, 공백을 한 칸 두고 모자를 쓸 수 있는 사람의 최대 수를 출력한다. 단, x는 테스트 케이스의 번호이다.

 