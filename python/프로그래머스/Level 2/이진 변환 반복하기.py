def solution(s):
    answer = [0, 0]
    while int(s) != 1:
        now = len(s)
        new_zero = "".join(s.split("0"))
        # 0제거 횟수 추가
        if now - len(new_zero) != 0:
            answer[1] += now - len(new_zero)
        binary_num = format(len(new_zero), "b")  # 2진수로 변환
        answer[0] += 1  # 변환했으니 하나 추가
        s = binary_num
    return answer
