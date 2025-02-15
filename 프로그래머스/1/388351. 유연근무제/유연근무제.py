def changeTime(time):
    return (time//100)*60 + time%100

def solution(schedules, timelogs, startday):
    N = len(schedules)
    answer = 0
    for i in range(N):
        schedule = changeTime(schedules[i])
        cnt = 0
        for j in range(7):
            today = (startday+j-1)%7
            if today == 5 or today == 6:
                continue
            timelog = changeTime(timelogs[i][j])
            if timelog <= schedule+10:
                cnt += 1
        if cnt == 5:
            answer += 1
    return answer