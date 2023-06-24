# 12. 침투(실2)

import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(M)]

def bfs(x, y):
  q = deque()
  q.append((x, y))
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if 0<=nx<M and 0<=ny<N:
        if arr[nx][ny] == 0:
          arr[nx][ny] = arr[x][y]+1
          q.append((nx, ny))
        
def isPercolate():
  for i in range(N):
    if arr[M-1][i] > 1:
      print("YES")
      return
  print("NO")
  return
  

for i in range(N):
  if arr[0][i] == 0:
    bfs(0, i)

isPercolate()