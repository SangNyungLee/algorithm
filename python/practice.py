#코드처리하기

def solution(code):
    answer = ''
    mode = 0
    for idx, alphabet in enumerate(code) :
        # alphabet == 1
        # mode =1 or 0 

        
        if alphabet == '1':
            # mode가 1이면 0, 0이면 1
            mode = 1 - mode
            continue
        #mode에 따라서 idx을 본다음에, answer에다가 answer+= alphabet
        if mode == 0 and idx % 2 == 0 :
            answer += alphabet
        elif mode == 1 and idx % 2 ==1 :
            answer += alphabet
    # 가장 쉽게 리턴하는 법
    if answer == "":
        answer = "EMPTY"
    return answer

    # 삼항연산자로 리턴 return answer if answer != "" else "EMPTY"
    # 파이썬에서 or 를 이용한 꼼수 return answer or "EMPTY" 로 바꿀 수 있다. 


# 숙련되거나 수학좀 친다
def solution2(code):
    return "".join(code.split("1"))[::2] or "EMPTY"