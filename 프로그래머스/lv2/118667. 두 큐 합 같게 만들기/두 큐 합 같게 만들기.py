from collections import deque

def solution(queue1, queue2):
    answer = 0
    total1 = sum(queue1)
    total2 = sum(queue2)
    total = (total1+total2)//2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    length = len(queue1)*3
    while True:
        if total1 > total2:
            queue2.append(queue1.popleft())
            total1 -= queue2[-1]
            total2 += queue2[-1]
        elif total1 < total2:
            queue1.append(queue2.popleft())
            total1 += queue1[-1]
            total2 -= queue1[-1]
        else:
            break
        answer += 1
        if answer > length:
            answer = -1
            break
        
    return answer