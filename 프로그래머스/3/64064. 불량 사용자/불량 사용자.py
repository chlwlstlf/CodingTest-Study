def isSame(str1, str2):
    for i in range(len(str1)):
        if str1[i] != '*':
            if str1[i] != str2[i]:
                return False
    return True

def dfs(result, visited, n, cnt, answer):
    if cnt == n:
        answer.add(tuple(visited))
        return
    for r in result[cnt]:
        if visited[r] == 0:
            visited[r] = 1
            dfs(result, visited, n, cnt+1, answer)
            visited[r] = 0

def solution(user_id, banned_id):
    n = len(banned_id)
    m = len(user_id)
    # banned_id에 해당하는 user_id 넣기
    result = [[] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if len(banned_id[i]) == len(user_id[j]):
                if isSame(banned_id[i], user_id[j]):
                    result[i].append(j)
    result.sort(key=lambda x: len(x))
    # 백트래킹
    answer = set()
    visited = [0]*m
    dfs(result, visited, n, 0, answer)
    return len(answer)