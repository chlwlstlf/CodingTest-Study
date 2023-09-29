def solution(s):
    answer = []
    s = s.replace("{", "[").replace("}", "]")
    s = eval(s)
    s.sort(key = lambda x: len(x))
    
    for i in range(len(s)):
        for j in range(len(s[i])):
            if s[i][j] not in answer:
                answer.append(s[i][j])
                break
    return answer