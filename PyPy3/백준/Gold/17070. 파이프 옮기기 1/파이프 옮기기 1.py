# 파이프 옮기기 1 (골5)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

if arr[N-1][N-1] == 1:
  print(0)
  exit()
      
def dfs(x, y, state):
  global cnt
  if x == N-1 and y == N-1 and arr[x][y] == 0:
    cnt += 1
    return
  if state == 0 or state == 2: # 가로, 대각선 → 가로
    if y+1 < N and arr[x][y+1] == 0:
      dfs(x, y+1, 0)
  if state == 1 or state == 2: # 세로, 대각선 → 세로 
    if x+1 < N and arr[x+1][y] == 0:
      dfs(x+1, y, 1)
  if x+1 < N and y+1 < N: # 모두 → 대각선 
    if arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0: 
      dfs(x+1, y+1, 2)

cnt = 0
dfs(0, 1, 0)
print(cnt)