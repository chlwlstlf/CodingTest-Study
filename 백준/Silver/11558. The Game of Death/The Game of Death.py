# 2. The Game of Death(실4)

import sys
input = sys.stdin.readline

T = int(input())

def dfs(p, visited, count):
  if p == N:
    print(count)
    return 
  if visited[p]:
    print(0)
    return 
  else :
    visited[p] = 1
    dfs(A[p-1], visited, count+1)


for i in range (T):
  N = int(input())
  A = [int(input()) for _ in range(N)]
  dfs(1, [0]*(N+1), 0)