# 1. 반복수열 (실4)

import sys
input = sys.stdin.readline

A, P = map(int, input().split())

def dfs(n, visited):
  if n in visited:
    print(visited.index(n))
    return 
  else :
    visited.append(n)

  num = list(map(int, str(n)))
  result = 0
  for i in range(len(num)):
    result += num[i]**P

  dfs(result, visited)
  

dfs(A, [])