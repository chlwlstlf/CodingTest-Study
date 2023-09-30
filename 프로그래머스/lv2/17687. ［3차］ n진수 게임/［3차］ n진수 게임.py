def notation(base, num):
    base16 = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = []
    while True:
        number = num%base
        if number >= 10:
            number = base16[number]
        result.append(str(number))
        num //= base
        if num == 0:
            break
    result.reverse()
    return result

def solution(n, t, m, p):
    answer2 = ''
    for i in range(t*m):
        answer2 += ''.join(notation(n, i))
        if len(answer2) >= t*m:
            break
        
    answer = ''
    for i in range(p-1, t*m, m):
        answer += answer2[i]
    return answer