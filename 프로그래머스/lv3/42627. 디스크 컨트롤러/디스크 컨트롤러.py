from heapq import heappush, heappop

def solution(jobs):
    answer = []
    l = len(jobs)
    time = 0
    waiting = []
    
    jobs.sort()

    while True:
        #time안에 실행할 수 있는 모든 작업을 waiting에 넣기
        while True:
            if jobs and jobs[0][0] <= time:
                heappush(waiting, (jobs[0][1], jobs[0][0])) #2열 기준으로 정렬됨
                heappop(jobs)
            else:
                break
        
        if waiting:
            answer.append(time-waiting[0][1]+waiting[0][0])
            time += waiting[0][0]
            heappop(waiting)
        else:
            time += 1
            
            
        if len(answer) == l:
            print(answer)
            break
        
    return sum(answer)//len(answer)