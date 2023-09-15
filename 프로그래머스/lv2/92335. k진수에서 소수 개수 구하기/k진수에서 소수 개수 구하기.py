from collections import deque
import math

def isPrime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    # k진법으로 바꾸기
    num = deque()
    while n > 0:
        num.appendleft(str(n%k))
        n //= k
    num = ''.join(num)
    
    #숫자 추출 & 소수 판별
    result = num.split('0')
    for r in result:
        if r:
            if int(r) != 1:
                answer += isPrime(int(r))
        
    return answer