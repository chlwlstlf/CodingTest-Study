# 2. 토마토 (골5)

import sys
from collections import deque
input = sys.stdin.readline

# 입력
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 1인 것 큐에 넣기
q = deque()
for i in range(N):
  for j in range(M):
    if arr[i][j] == 1:
      q.append((i, j))

# bfs
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M:
      if arr[nx][ny] == 0:
        arr[nx][ny] = arr[x][y] + 1
        q.append((nx, ny))

# 출력
for i in range(N):
  for j in range(M):
    if arr[i][j] == 0:
      print(-1)
      sys.exit()
print(max(max(a) for a in arr)-1)
