import sys
input = sys.stdin.readline

N, M = map(int, input().split())
U = [i+1 for i in range(N)]

def dfs(cnt, arr):
  if cnt == M:
    print(' '.join(map(str, arr)))
    return
  for i in range(N):
    if len(arr) == 0 or arr[-1] <= U[i]:
      arr.append(U[i])
      dfs(cnt+1, arr)
      arr.pop()

dfs(0, [])