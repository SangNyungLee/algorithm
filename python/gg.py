def rotate_left(lst): # 반시계 방향 회전 (-1)
    lst.append(lst.popleft())

def rotate_right(lst):
     lst.appendleft(lst.pop()) # 시계 방향 회전

from collections import deque
wheel = [deque()] # 톱니바퀴 번호 1번 부터 시작
for _ in range(4):
    wheel.append(deque(map(int, input())))

K = int(input()) # 회전 수 

arr = deque()
for _ in range(K):
    a,b = map(int, input().split())
    arr.append((a,b)) # 톱니바퀴 번호, 회전 방향
# 항상 순서는 맞닿은 부분이 서로 다른지 체크하고 돌리고 -> 시작 톱니바퀴 돌리기
# (2) - (6 - 2) - (6 - 2) - (6)
while arr:
    wheel_number, rotate_direction = arr.popleft()
    # 1번 일 때는 6번이랑 맞는지 확인하기
    if wheel_number == 1:
        # 만약에 둘이 다르면 그 뒤에 애들까지 전부 체크하기
        if wheel[1][2] != wheel[2][6]:
            # 2번, 3번 같고, 3번, 4번까지 모두 다르면 다 돌려버리셈
            if wheel[2][2] != wheel[3][6] and wheel[3][2] != wheel[4][6]:
                if rotate_direction == 1:
                    rotate_left(wheel[2])
                    rotate_right(wheel[3])
                    rotate_left(wheel[4])
                else:
                    rotate_right(wheel[2])
                    rotate_left(wheel[3])
                    rotate_right(wheel[4])

            # 2번 != 3번, 3번 == 4번 3번만 돌림
            elif wheel[2][2] != wheel[3][6] and wheel[3][2] == wheel[4][6]:
                if rotate_direction == 1:
                    rotate_left(wheel[2])
                    rotate_right(wheel[3])
                else:
                    rotate_right(wheel[2])
                    rotate_left(wheel[3])
            elif wheel[2][2] == wheel[3][6] and wheel[3][2] == wheel[4][6]:
                if rotate_direction == 1:
                    rotate_left(wheel[2])
                else:
                    rotate_right(wheel[2])
        if rotate_direction == 1:
            rotate_right(wheel[1])
        else:
            rotate_left(wheel[1])
    # 4번을 돌릴 때        
    elif wheel_number == 4:
        # 4번과 맞닿은 3번이 다를 때
        if wheel[4][6] != wheel[3][2]:
            # 2,3 다르고, 1,2까지 다르면 전부 다 돌려버리기
            if wheel[2][2] != wheel[3][6] and wheel[1][2] != wheel[2][6]:
                if rotate_direction == 1:
                    rotate_left(wheel[3])
                    rotate_right(wheel[2])
                    rotate_left(wheel[1])
                else:
                    rotate_right(wheel[3])
                    rotate_left(wheel[2])
                    rotate_right(wheel[1])
            elif wheel[2][2] != wheel[3][6] and wheel[1][2] != wheel[2][6]:
                if rotate_direction == 1:
                    rotate_left(wheel[3])
                    rotate_right(wheel[2])
                else:
                    rotate_right(wheel[3])
                    rotate_left(wheel[2])
        # 할일 다 하고 마지막에 돌려주면 됨    
        if rotate_direction == 1:
            rotate_right(wheel[4])
        else:
            rotate_left(wheel[4])
    # 2번 돌리는 경우
    elif wheel_number == 2:
        # 2번이랑 1번이랑 다른 경우(얘는 다른 애들한테 영향 x)
        if wheel[1][2] != wheel[2][6]:
            if rotate_direction == 1:
                rotate_left(wheel[1])
            else:
                rotate_right(wheel[1])
        # 2번이랑 3번이랑 다르고 , 3번이랑 4번이랑 다른 경우
        if wheel[2][2] != wheel[3][6] and wheel[3][2] != wheel[4][6]:
            if rotate_direction == 1:
                rotate_left(wheel[3])
                rotate_right(wheel[4])
            else:
                rotate_right(wheel[3])
                rotate_left(wheel[4])
        # 2번이랑 3번이랑 다르고, 3번이랑 4번이랑 같은 경우
        elif wheel[2][2] != wheel[3][6] and wheel[3][2] == wheel[4][6]:
            if rotate_direction == 1:
                rotate_left(wheel[3])
            else:
                rotate_right(wheel[3])
        # 마지막에는 자기 자신 돌리기
        if rotate_direction == 1:
            rotate_right(wheel[2])
        else:
            rotate_left(wheel[2])
    # 3번 돌리는 경우
    elif wheel_number == 3:
        # 3번이랑 4번이랑 다른 경우(4번은 다르던 같던 다른 애들한테 영향 안줌)
        if wheel[3][2] != wheel[4][6]:
            if rotate_direction == 1:
                rotate_left(wheel[4])
            else:
                rotate_right(wheel[4])
        # 2번이랑 3번이랑 다르고, 1번이랑 2번이랑 다른 경우
        if wheel[2][2] != wheel[3][6] and wheel[1][2] != wheel[2][6]:
            if rotate_direction == 1:
                rotate_left(wheel[2])
                rotate_right(wheel[1])
            else:
                rotate_right(wheel[2])
                rotate_left(wheel[1])
        # 2번이랑 3번이랑 다르고 1번이랑 2번이랑 같은 경우
        elif wheel[2][2] != wheel[3][6] and wheel[1][2] == wheel[2][6]:
            if rotate_direction ==1:
                rotate_left(wheel[2])
            else:
                rotate_right(wheel[2])
        if rotate_direction == 1:
            rotate_right(wheel[3])
        else:
            rotate_left(wheel[3])
answer = 0
for i in range(1,5):
    if wheel[i][0] == 1:
        answer += 2**(i-1)
print(answer)