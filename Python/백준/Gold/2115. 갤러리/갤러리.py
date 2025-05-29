# 갤러리 (골5)

import sys
input = sys.stdin.readline


def solve():
  N, M = map(int, input().split())
  arr = [list(input().rstrip()) for _ in range(N)]

  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  result = [[[0]*4 for _ in range(M)] for _ in range(N)]
  for i in range(N):
    for j in range(M):
      if arr[i][j] == "X":
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == ".":
            result[i][j][k] = 1

  answer = 0
  for i in range(N):
    for j in range(M):
      if result[i][j][0] == 1: # 북쪽에 . 이 있음: 오른쪽과 비교
        if j+1 < M and result[i][j+1][0] == 1:
          result[i][j][0] = 0
          result[i][j+1][0] = 0
          answer += 1
      if result[i][j][1] == 1: # 남쪽에 . 이 있음: 오른쪽과 비교
        if j+1 < M and result[i][j+1][1] == 1:
          result[i][j][1] = 0
          result[i][j+1][1] = 0
          answer += 1    
      if result[i][j][2] == 1: # 서쪽에 . 이 있음: 아래쪽과 비교
        if i+1 < N and result[i+1][j][2] == 1:
          result[i][j][2] = 0
          result[i+1][j][2] = 0
          answer += 1    
      if result[i][j][3] == 1: # 동쪽에 . 이 있음: 아래쪽과 비교
        if i+1 < N and result[i+1][j][3] == 1:
          result[i][j][3] = 0
          result[i+1][j][3] = 0
          answer += 1 
  return answer

print(solve())