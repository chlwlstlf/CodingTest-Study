def solution(msg):
    answer = []
    dict = {}
    for i in range(26):
        dict[chr(ord('A')+i)] = i+1
        
    i = 0
    j = 27
    c = msg[0]
    while True:
        w = c
        for k in range(i+1, len(msg)):
            w += msg[k]
            if w not in dict:
                dict[w] = j
                j += 1
                c = w[-1]
                w = w[:-1]
                break
        answer.append(dict[w])
        i += len(w)
        if i >= len(msg):
            break
            
    return answer