def change(n):
    result = ""
    while n > 0:
        n -= 1  
        result += chr(n % 26 + ord('a'))
        n //= 26 
    return result[::-1]

def solution(n, bans):
    bans.sort()
    N = n+len(bans)
    answer = change(N)
    
    prev = -1
    while True:
        cnt = 0
        for b in bans:
            if len(b) > len(answer):
                cnt += 1
            if len(b) == len(answer) and b >= answer:
                cnt += 1
        if cnt == prev:
            return answer
        answer = change(N-cnt)
        prev = cnt
