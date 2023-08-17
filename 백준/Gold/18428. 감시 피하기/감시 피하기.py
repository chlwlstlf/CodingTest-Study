# 4. 감시 피하기 (골5)

import sys
import copy
from itertools import combinations
input = sys.stdin.readline

N = int(input())
arr = [list(input().split()) for _ in range(N)]

# 장애물 설치한 후 감시 여부 확인 함수
def check(array):
  for t in T:
    for i in range(4):
      nx, ny = t
      while True:
        nx += dx[i]
        ny += dy[i]
        if 0 <= nx < N and 0 <= ny < N:
          if array[nx][ny] == 'S':
              return False
          if array[nx][ny] == 'O':
              break
        else:
          break
  return True

# T일 때 obstacle 함수 호출
T = [] # 선생님 위치
O = [] # 장애물 설치 가능한 위치
for i in range(N):
  for j in range(N):
    if arr[i][j] == 'T':
      T.append((i, j))
    elif arr[i][j] != 'S':
      O.append((i, j))

# 3개 위치를 골라서 장애물 설치
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
com = list(combinations(O, 3))

if len(com) == 1:
  print("YES")
  sys.exit()
for c in com:
  a = copy.deepcopy(arr)
  for i in range(3):
    a[c[i][0]][c[i][1]] = 'O'
  if check(a):
    print("YES")
    sys.exit()
print("NO")
