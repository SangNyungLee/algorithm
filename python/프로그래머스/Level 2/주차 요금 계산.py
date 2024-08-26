def solution(fees, records):
    queue = []
    answer = []
    dic = {}
    for i in records:
        time, car_num, entry = i.split()
        car_num = int(car_num)
        hour, minute = time.split(":")
        cal_time = (int(hour) * 60) + int(minute)  # 시간 계산
        if entry == "IN":
            if car_num not in dic:
                dic[car_num] = 0
            queue.append((car_num, cal_time))
        else:  # entry == OUT일 때
            for j in range(len(queue)):
                if queue[j][0] == car_num:
                    total_time = cal_time - queue[j][1]
                    dic[car_num] += total_time
                    queue.pop(j)
                    break
    # 다 나가고 queue 확인
    while queue:
        x, y = queue.pop()
        dic[x] += 1439 - y
    dic_item = sorted(dic.items())
    for x, y in dic_item:
        if y <= fees[0]:
            answer.append(fees[1])
        else:
            y -= fees[0]
            if y % fees[2] == 0:
                y = y // fees[2]
                answer.append(y * fees[3] + fees[1])
            else:
                y = y // fees[2]
                answer.append(((y + 1) * fees[3]) + fees[1])
    return answer
