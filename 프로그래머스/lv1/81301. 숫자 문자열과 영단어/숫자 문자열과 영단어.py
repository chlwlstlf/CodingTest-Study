def solution(s):
    #딕셔너리 만들기
    dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    #계산
    i = 0
    answer = ''
    while i < len(s):
        if s[i] >= '0' and s[i] <= '9':
            answer += s[i]
            i += 1 
        else:
            for key in dict:
                if key in s[i:min(i+5, len(s))]:
                    answer += dict[key]
                    i += len(key)
                    break
                    
    return int(answer)