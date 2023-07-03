# 1. 점프 점프(실2)

import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
s = int(input())

def dfs(v):
  visited[v] = 1
  if 0 <= v-A[v] < n:
    if visited[v-A[v]] == 0:
      dfs(v-A[v])
  if 0 <= v+A[v] < n:
    if visited[v+A[v]] == 0:
      dfs(v+A[v])

visited = [0]*n
dfs(s-1)
print(visited.count(1))