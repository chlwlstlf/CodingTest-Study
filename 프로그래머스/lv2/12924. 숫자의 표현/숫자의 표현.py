def solution(n):
    answer = 0
    
    for i in range(0, n+1):
        result = 0
        start = i
        while True:
            start += 1
            result += start
            if result == n:
                answer += 1
            elif result > n:
                break
    
    return answer