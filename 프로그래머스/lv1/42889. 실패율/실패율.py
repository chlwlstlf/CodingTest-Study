def solution(N, stages):
    # 계수 정렬로 스테이지 개수 구하기
    num = [0]*(N+1)
    for i in range(len(stages)):
        num[stages[i]-1] += 1
        
    # 실패율 구하기
    answer = []
    length = len(stages)
    total = 0
    for i in range(N):
        if length-total == 0:
            answer.append((i+1, 0))
        else:
            answer.append((i+1, num[i]/(length-total)))
        total += num[i]
    answer.sort(key = lambda x: (-x[1], x[0]))
    answer = [answer[i][0] for i in range(N)]
    return answer