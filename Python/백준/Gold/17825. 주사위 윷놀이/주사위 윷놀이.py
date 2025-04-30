# 주사위 윷놀이 (골2)

import sys
input = sys.stdin.readline

position = list(map(int, input().split()))

per = [0]*10
answer = 0

score = [[] for _ in range(4)]
score[0] = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 42, 42, 42, 42]
score[1] = [10, 13, 16, 19, 25, 30, 35, 40, 42, 42, 42, 42, 42]
score[2] = [20, 22, 24, 25, 30, 35, 40, 42, 42, 42, 42, 42]
score[3] = [30, 28, 27, 26, 25, 30, 35, 40, 42, 42, 42, 42, 42]

def solve(arr):
  ans = 0
  result = [[0, 0], [0, 0], [0, 0], [0, 0]]
  for i in range(10):
    curMal = arr[i]
    x, y = result[curMal]

    # 도착한 말을 움직일 수 없으므로 return -1
    if score[x][y] == 42:
      return -1
    
    # 말 이동
    cy = y + position[i]
    nx, ny = x, cy
    if x == 0:
      if score[nx][ny] == 10 or score[nx][ny] == 20 or score[nx][ny] == 30:
        nx, ny = score[nx][ny]//10, 0

    # 도착하면 점수 계산 x
    if score[nx][ny] == 42:
      result[curMal] = [nx, ny]
      continue

    # 이동한 위치에 말이 있다면 return -1, 도착 이후면 점수 그대로
    curScore = score[nx][ny]
    for j in range(4):
      diffx, diffy = result[j][0], result[j][1]
      if curMal == j: # 자기 말이면 비교x
        continue
      if score[nx][ny] == score[diffx][diffy] == 40: # 40이면
        return -1
      if nx > 0 and ny > 0 and diffx > 0 and diffy > 0: # 25, 30, 35면
        if score[nx][ny] == score[diffx][diffy] == 25:
          return -1
        if score[nx][ny] == score[diffx][diffy] == 30:
          return -1
        if score[nx][ny] == score[diffx][diffy] == 35:
          return -1
      if nx == diffx and ny == diffy: # 위치가 같으면
        return -1

    result[arr[i]] = [nx, ny]
    ans += curScore
  return ans

def dfs(v):
  global answer
  if v == 10:
    answer = max(answer, solve(per))
    return
  for i in range(0, 4):
    per[v] = i
    dfs(v+1)

dfs(0)
print(answer)