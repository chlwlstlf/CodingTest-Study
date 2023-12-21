# 1. 인구 이동 (골4)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, L, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 연합하기 - dfs
def dfs(x, y):
  global total, cnt
  if visited[x][y] == 0:
    visited[x][y] = 1
    total += A[x][y]
    cnt += 1
    index.append((x, y))
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < N:
        if L <= abs(A[x][y] - A[nx][ny]) <= R:
          dfs(nx, ny)
    return True
  return False

# 인구 이동 반복
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while True:
  count = 0
  # 연합하기
  visited = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      total, cnt = 0, 0
      index = []
      if dfs(i, j):
        result = total//cnt
        for k in index:
          A[k[0]][k[1]] = result
      if cnt > 1:
        count += 1
  if count == 0:
    print(answer)
    break
  answer += 1
