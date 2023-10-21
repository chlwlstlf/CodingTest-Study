def solution(s):
    #딕셔너리 만들기
    dict = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    #숫자로 바꿔주기
    for key, value in dict.items():
        s = s.replace(key, value)           
    return int(s)