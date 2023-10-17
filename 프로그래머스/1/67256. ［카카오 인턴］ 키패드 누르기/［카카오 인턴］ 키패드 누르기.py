# 2. [카카오 인턴] 키패드 누르기

def solution(numbers, hand):
    # 디폴트값 설정
    keypad = {1: (0, 0), 2: (0, 1), 3: (0, 2), 
              4: (1, 0), 5: (1, 1), 6: (1, 2), 
              7: (2, 0), 8: (2, 1), 9: (2, 2),
             '*': (3, 0), 0: (3, 1), '#': (3, 2)}
    fixed = {1: 'L', 3: 'R', 4: 'L', 6: 'R', 7: 'L', 9: 'R'}
    current = {'L': '*', 'R': '#'}
    if hand == 'left': flag = 'L'
    else: flag = 'R'
    
    # 계산 하기
    answer = ''
    for n in numbers:
        # 왼손 또는 오른손 고정
        if n in fixed:
            answer += fixed[n]
            current[fixed[n]] = n
        # 가운데 누를 때 
        else:
            x = keypad[n][0]
            y = keypad[n][1]
            L_dist = abs(keypad[current['L']][0]-x) + abs(keypad[current['L']][1]-y)
            R_dist = abs(keypad[current['R']][0]-x) + abs(keypad[current['R']][1]-y)
            if L_dist < R_dist:
                answer += 'L'
                current['L'] = n
            elif L_dist > R_dist:
                answer += 'R'
                current['R'] = n
            else:
                answer += flag
                current[flag] = n
    return answer