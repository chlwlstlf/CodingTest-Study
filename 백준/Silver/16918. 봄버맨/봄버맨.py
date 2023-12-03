# 3. 봄버맨 (실1)

import sys
input = sys.stdin.readline

# 입력
R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

# 'O'를 0으로 바꾸기(0초에 설치된 폭탄이라는 뜻)
for i in range(R):
  for j in range(C):
    if arr[i][j] == 'O':
      arr[i][j] = 0

# 폭탄 설치 함수
def installBomb(t):
  for i in range(R):
    for j in range(C):
      if arr[i][j] == '.':
        arr[i][j] = t

# 폭탄 폭발 함수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def explosionBomb(t):
  for i in range(R):
    for j in range(C):
      if arr[i][j] == t:
        arr[i][j] = '.'
        for k in range(4):
          nx = i+dx[k]
          ny = j+dy[k]
          if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != t:
            arr[nx][ny] = '.'

# for문으로 time 돌리기
for time in range(2, N+1):
  if time%2 == 0:
    installBomb(time)
  else:
    explosionBomb(time-3)

# 출력
for i in range(R):
  for j in range(C):
    if arr[i][j] == '.':
      print('.', end='')
    else:
      print('O', end='')
  print()

