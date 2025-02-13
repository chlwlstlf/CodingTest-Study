def solution(n, w, num):
    arr = []
    for i in range(n//w+1):
        if i%2 == 0:
            a = [w*i+j for j in range(1, w+1)]
        else:
            a = [w*i+j for j in range(w, 0, -1)]
        arr.append(a)
        
    for i in range(n//w+1):
        for j in range(w):
            if arr[i][j] == num:
                x, y = i, j
                break
                
    answer = 0            
    for i in range(x, n//w+1):
        if arr[i][y] <= n:
            answer += 1
    return answer