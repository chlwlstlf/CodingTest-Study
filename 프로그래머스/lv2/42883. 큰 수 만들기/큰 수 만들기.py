def solution(number, k):
    n = list(map(int, str(number)))
    total = len(n)-k
    idx = 0
    answer = ''
    while True:
        end = len(n)-total+1
        
        max = 0
        for i in range(idx,end):
            if n[i] == 9:
                max = n[i]
                id = i+1
                break
            if n[i] > max:
                max = n[i]
                id = i+1
        
        answer += str(max)
        idx = id
        total -= 1
        
        if total == 0 or len(n)-idx==total:
            break
            
    if total > 0:
        answer += ''.join(map(str, n[idx:len(n)]))
    
    return answer
