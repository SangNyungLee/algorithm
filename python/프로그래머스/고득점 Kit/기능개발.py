def solution(progresses, speeds):
    answer = []
    while progresses:
        if progresses[0] >= 100:
            cnt = 0
            while True:
                if progresses and progresses[0] >= 100:
                    cnt += 1
                    progresses.pop(0)
                    speeds.pop(0)
                else:
                    answer.append(cnt)
                    break
        for i in range(len(speeds)):
            progresses[i] += speeds[i]
    return answer
