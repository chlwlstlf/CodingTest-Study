# 특별상이라도 받고 싶어 (실3)

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

if N == 1:
  print(arr[0][0])
  exit()

def dfs(x, y, n):
  if n == 1:
    return arr[x][y]
  else:
    min = []
    min.append(dfs(x, y, n//2))
    min.append(dfs(x, y+n//2, n//2))
    min.append(dfs(x+n//2, y, n//2))
    min.append(dfs(x+n//2, y+n//2, n//2))
    min.sort()
    return min[1]

print(dfs(0, 0, N))