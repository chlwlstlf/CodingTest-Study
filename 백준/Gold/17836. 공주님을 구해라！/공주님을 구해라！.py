# 3. 공주님을 구해라! (골5)

import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M, T = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(N)]
arr2 = copy.deepcopy(arr1)

# bfs1 - 검 상관x
def bfs1(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and arr1[nx][ny] in (0, 2):
        arr1[nx][ny] = arr1[x][y] + 1
        q.append((nx, ny))

# bfs2 - 검 획득
def bfs2(x, y):
  q = deque()
  q.append((x, y))
  visited = [[0]*M for _ in range(N)]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if arr2[nx][ny] == 0:
          arr2[nx][ny] = arr2[x][y] + 1
          q.append((nx, ny))
          visited[nx][ny] = 1
        if arr2[nx][ny] == 2 and visited[nx][ny] == 0: 
          arr2[N-1][M-1] = arr2[x][y] + 1 + N-nx-1 + M-ny-1
          return

# bfs 호출
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
bfs1(0, 0)
bfs2(0, 0)

# 출력
min_value = min(arr1[N-1][M-1], arr2[N-1][M-1])
max_value = max(arr1[N-1][M-1], arr2[N-1][M-1])
if min_value == 0:
  if max_value == 0 or max_value > T:
    print("Fail")
  else:
    print(max_value)
else:
  if min_value > T:
    print("Fail")
  else:
    print(min_value)
  