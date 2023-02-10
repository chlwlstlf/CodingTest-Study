def solution(brown, yellow):
    i = 1
    while True:
        j = yellow/i
        if (i+2)*(j+2) == (brown+yellow):
            answer = [i+2, j+2]
            break
        i += 1
    answer.sort(reverse=True)
    return answer