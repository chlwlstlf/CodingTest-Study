import math

def solution(progresses, speeds):
    answer = []
    time = math.ceil((100.0-progresses[0])/speeds[0])
    count = 0
    
    for i in range(len(progresses)):
        if math.ceil((100.0-progresses[i])/speeds[i]) > time:
            answer.append(count)
            count = 0
            time = math.ceil((100.0-progresses[i])/speeds[i])
        count += 1
    answer.append(count)
    return answer