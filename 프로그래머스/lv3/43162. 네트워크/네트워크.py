def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    
    def dfs(v):
        nonlocal cnt
        visited[v] = 1
        cnt += 1
        for i in graph[v]:
            if visited[i] == 0:
                dfs(i)
            
                
    #그래프 생성
    for i in range(len(computers)):
        for j in range(i+1, len(computers)):
            if computers[i][j] == 1:
                graph[i+1].append(j+1)
                graph[j+1].append(i+1)
    
    #dfs 부르기
    for i in range(len(computers)):
        cnt = 0
        if visited[i+1] == 0:
            dfs(i+1)
            answer += 1
            print(visited)
            
    return answer