# 3. 봄버맨(실1)

import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

if N%2 == 0:
  for i in range(R):
    print('O'*C)
else:
  dx = [1, -1, 0, 0]
  dy = [0, 0, 1, -1]

  #계산을 해주기 위해 'O'을 0으로 바꿈
  for i in range(R):
    for j in range(C):
      if arr[i][j] == 'O':
        arr[i][j] = 0

  for i in range(2, N+1):
    if i%2 == 0:
      for j in range(R):
        for k in range(C):
          if arr[j][k] == '.':
            arr[j][k] = i
    else:
      for j in range(R):
        for k in range(C):
          if arr[j][k] == i-3:
            arr[j][k] = '.'
            for l in range(4):
              if 0<=j+dx[l]<R and 0<=k+dy[l]<C and arr[j+dx[l]][k+dy[l]] != i-3:
                arr[j+dx[l]][k+dy[l]] = '.'
  #출력
  for i in range(R):
    for j in range(C):
      if arr[i][j]=='.':
        print('.', end='')
      else:
        print('O', end='')
    print()