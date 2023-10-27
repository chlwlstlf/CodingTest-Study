def solution(gems):
    type = list(set(gems))
    dict = {}
    current, start, end = 0, 0, 0
    length = len(gems)
    # current는 계속 늘어나지만 start와 end의 값은 최소 길이가 아닌 이상 갱신되지 않는다.
    for i in range(len(gems)):
        # dict 값 갱신
        if gems[i] in dict:
            dict[gems[i]] += 1
        else:
            dict[gems[i]] = 1
        # 모든 보석이 1개 이상일 때
        if len(dict) == len(type):
            for j in range(current, i):
                if dict[gems[j]] > 1:
                    dict[gems[j]] -= 1
                else:
                    current = j
                    break
            if i-current < length:
                length = i-current
                start = current
                end = i
    return [start+1, end+1]