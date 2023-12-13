# 1. 쉬운 최단거리 (실1)

import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]

# bfs
def bfs(x, y):
  q = deque()
  q.append((x, y))
  arr[x][y] = 0
  visited[x][y] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if arr[nx][ny] == 1 and visited[nx][ny] == 0:
          arr[nx][ny] = arr[x][y] + 1
          visited[nx][ny] = 1
          q.append((nx, ny))

# bfs 호출
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
f = 0
for i in range(n):
  for j in range(m):
    if arr[i][j] == 2:
      bfs(i, j)
      f = 1
      break
  if f == 1:
    break

# -1 변환
for i in range(n):
  for j in range(m):
    if arr[i][j] == 1 and visited[i][j] == 0:
      arr[i][j] = -1

# 출력
for a in arr:
  print(*a)