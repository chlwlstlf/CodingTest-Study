from itertools import combinations

def solve(c, q, ans):
    N = len(q)
    for i in range(N):
        if len(set(list(c)+q[i])) != 10-ans[i]:
            return False
    return True

def solution(n, q, ans):
    answer = 0
    combs = list(combinations([i+1 for i in range(n)], 5))
    for c in combs:
        answer += solve(c, q, ans)
    return answer