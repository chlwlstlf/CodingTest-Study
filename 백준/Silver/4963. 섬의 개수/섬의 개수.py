# 2. 섬의 개수(실2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(x, y):
  if x < 0 or x >= h or y < 0 or y >= w:
    return False
  
  if m[x][y] == 1:
    m[x][y] = 0
    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    dfs(x-1, y-1)
    dfs(x+1, y-1)
    dfs(x+1, y+1)
    dfs(x-1, y+1)
    return True

  return False


while True:
  w, h  = map(int, input().split())
  if w== 0 and h == 0:
    break

  m = [list(map(int, input().split())) for _ in range(h)]
  
  cnt = 0
  for i in range(h):
    for j in range(w):
      if dfs(i, j) == True:
        cnt += 1
  
  print(cnt)
