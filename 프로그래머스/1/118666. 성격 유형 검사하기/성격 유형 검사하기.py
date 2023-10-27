def solution(survey, choices):
    # 초깃값
    dict = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    keys = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    scores = [0, 3, 2, 1, 0, 1, 2, 3]
    # 각 mbti의 점수 구하기
    for i in range(len(survey)):
        score = scores[choices[i]]
        if choices[i] < 4:
            dict[survey[i][0]] += score
        else:
            dict[survey[i][1]] += score
    # answer에 mbti 넣기
    answer = ''
    for i in range(0, 8, 2):
        answer += keys[i] if dict[keys[i]] >= dict[keys[i+1]] else keys[i+1]       
    return answer