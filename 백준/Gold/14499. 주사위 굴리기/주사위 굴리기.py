# 4. 주사위 굴리기(골4)

import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]
dir = [[4, 2, 1, 6, 5, 3], [3, 2, 6, 1, 5, 4], [5, 1, 3, 4, 6, 2], [2, 6, 3, 4, 1, 5]]

for i in range(K):
  o = order[i]-1
  # 주사위 위치 바꾸기
  x = x + dx[o]
  y = y + dy[o]
  if x < 0 or x >= N or y < 0 or y >= M:
    x = x - dx[o]
    y = y - dy[o]
    continue
  # 주사위 상태 바꾸기
  d = dice[:]
  for j in range(6):
    dice[j] = d[dir[o][j]-1]
  # 숫자 복사
  if arr[x][y] == 0:
    arr[x][y] = dice[5]
  else:
    dice[5] = arr[x][y]
    arr[x][y] = 0
  print(dice[0])