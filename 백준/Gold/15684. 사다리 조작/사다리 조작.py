# 1. 사다리 조작 (골3)

import sys
input = sys.stdin.readline

# 입력 & 사다리 만들기
N, M, H = map(int, input().split())
ladder = [[0 for _ in range(N+1)] for _ in range(H+1)]
for i in range(M):
  a, b = map(int, input().split())
  ladder[a][b] = 1

# 사다리 타기
def ghostLeg(v):
  for i in range(1, H+1):
    if ladder[i][v] == 1:
      v += 1
      continue
    if ladder[i][v-1] == 1:
      v -= 1
      continue
  return v

# N개 다 자기 자신으로 가는지 여부 반환하기
def isPossible():
  for v in range(1, N+1):
    if v != ghostLeg(v):
      return False
  return True

# 백트래킹
def backtracking(depth, x, y):
  global answer
  if depth == 4:
    return
  if isPossible():
    answer = min(answer, depth)
    return
  for i in range(x, H+1):
    k = y if i == x else 1
    for j in range(k, N):
      if ladder[i][j] == 0 and ladder[i][j+1] == 0:
        ladder[i][j] = 1
        backtracking(depth+1, i, j+2)
        ladder[i][j] = 0

# 출력
answer = 4
backtracking(0, 1, 1)
print(-1 if answer == 4 else answer)