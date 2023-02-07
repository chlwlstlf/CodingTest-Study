def solution(answers):
    answer = []
    result = []
    s = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        cnt = 0
        for j in range(len(answers)):
            if answers[j] == s[i][j%len(s[i])]:
                cnt += 1
        result.append(cnt)
        
    for i in range(3):
        if max(result) == result[i]:
            answer.append(i+1)
    return answer