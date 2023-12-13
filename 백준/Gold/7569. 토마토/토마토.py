# 3. 토마토 (골5)

import sys
from collections import deque
input = sys.stdin.readline

# 입력
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 1인 것 큐에 넣기
q = deque()
for i in range(H):
  for j in range(N):
    for k in range(M):
      if arr[i][j][k] == 1:
        q.append((i, j, k))

# bfs
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
while q:
  x, y, z = q.popleft()
  for i in range(6):
    nx = x + dx[i]
    ny = y + dy[i]
    nz = z + dz[i]
    if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M:
      if arr[nx][ny][nz] == 0:
        arr[nx][ny][nz] = arr[x][y][z] + 1
        q.append((nx, ny, nz))

# 출력
answer = 0
for i in range(H):
  for j in range(N):
    for k in range(M):
      if arr[i][j][k] == 0:
        print(-1)
        sys.exit()
      answer = max(answer, arr[i][j][k])
print(answer-1)
