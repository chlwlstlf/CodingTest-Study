# 1. 아기 상어 2(실2)

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(N)]

def bfs():
  while q :
    x, y = q.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue

      if S[nx][ny] == 0:
        S[nx][ny] = S[x][y] + 1
        q.append((nx, ny))
      

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]

q = deque()
for i in range(N):
  for j in range(M):
    if S[i][j] == 1:
      q.append((i, j))

bfs()
result = 0
for i in range(N):
  for j in range(M):
    if S[i][j] > result:
      result = S[i][j]
print(result-1)