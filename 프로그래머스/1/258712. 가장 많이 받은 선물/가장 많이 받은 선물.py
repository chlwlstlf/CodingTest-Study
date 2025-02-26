def solution(friends, gifts):
    dict = {}
    N = len(friends)
    for i in range(N):
        dict[friends[i]] = i 
        
    arr = [[0]*N for _ in range(N)]
    for g in gifts:
        x, y = g.split(" ")
        arr[dict[x]][dict[y]] += 1
        
    index = [[0, 0, 0] for _ in range(N)]
    for i in range(N):
        index[i][0] = sum(arr[i])
        index[i][1] = sum([arr[j][i] for j in range(N)])
        index[i][2] = index[i][0]-index[i][1]

    answer = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] > arr[j][i]:
                cnt += 1
            if arr[i][j] == arr[j][i]:
                if index[i][2] > index[j][2]:
                    cnt += 1
        answer = max(answer, cnt)                  
    return answer