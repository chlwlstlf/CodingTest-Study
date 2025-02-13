def solution(players, m, k):
    answer = []
    for p in players:
        cnt = 0
        for i in range(len(answer)):
            if answer[i] > 0:
                answer[i] -= 1
            if answer[i] > 0:
                cnt += 1
        if p//m > cnt:
            answer += [k]*(p//m-cnt)
    return len(answer)