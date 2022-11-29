# 8. 체스판 다시 칠하기 (실4) 모르겠음

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for i in range (N):
  board.append(list(input().rstrip()))

result = N*M
for i in range (N-7):
  for j in range (M-7):
    cnt_b = 0 #첫 값이 B일 때 개수
    cnt_w = 0 #첫 값이 W일 때 개수
    for k in range(8):
      for l in range(8):
        if (i+j+k+l)%2 == (i+j)%2: 
          if board[i+k][j+l] == 'B': 
            cnt_w += 1
          else: 
            cnt_b += 1
        if (i+j+k+l)%2 != (i+j)%2: 
          if board[i+k][j+l] == 'W': 
            cnt_w += 1
          else: 
            cnt_b += 1
    if min(cnt_b, cnt_w) < result:
      result = min(cnt_b, cnt_w)
print(result)
