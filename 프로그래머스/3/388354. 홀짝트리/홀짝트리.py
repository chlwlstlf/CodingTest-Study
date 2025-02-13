visited = [0]*(1000001)
root = [-1]*(1000001)

def dfs(v, graph):
    result = []
    stack = [v]
    while stack:
        v = stack.pop()
        result.append(v)
        if visited[v] == 1:
            continue
        visited[v] = 1
        root[v] = 0 if v%2 == len(graph[v])%2 else 1
        for i in graph[v]:
            if visited[i] == 0:
                stack.append(i)
    
    answer = [0, 0]
    total = [0, 0]
    for r in result:
        total[root[r]] += 1
    if total[0] == 1:
        answer[0] += 1
    if total[1] == 1:
        answer[1] += 1
    return answer

def solution(nodes, edges):
    # 그래프 생성
    N, M = max(nodes), len(edges)
    graph = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = edges[i]
        graph[a].append(b)
        graph[b].append(a)

    # 그래프 분리
    answer = [0, 0]
    for n in nodes:
        if visited[n] == 0:
            x, y = dfs(n, graph)
            answer[0] += x
            answer[1] += y
    return answer