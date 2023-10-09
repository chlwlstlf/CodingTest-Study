def isTen(arr):
    if arr[0] == '1' and arr[1] == '0': # 10일 때
        arr[0] = '10'
        del arr[1]
    return arr

def solution(dartResult):
    # `점수|보너스|[옵션]`으로 나누기
    result = []
    idx = 0
    for i in range(1, len(dartResult)):
        if dartResult[i] >= '0' and dartResult[i] <= '9' and i > idx+1:
            result.append(isTen(list(dartResult[idx:i])))
            idx = i
    result.append(isTen(list(dartResult[idx:len(dartResult)])))
    
    # 스타상 적용
    for i in range(1, len(result)):
        if len(result[i]) >= 3:
            if result[i][2] == '*':
                result[i-1].append(result[i][2])
                
    # 최종 계산
    answer = 0
    dict = {'S': 1, 'D': 2, 'T': 3, '*': 2, '#': -1}
    for r in result:
        n = int(r[0])**dict[r[1]]
        for i in range(2, len(r)):
            n *= dict[r[i]]
        answer += n
    return answer