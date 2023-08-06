# 2. 치즈 (골3)

import sys
from collections import deque
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# bfs 외부공기 2로 만들기
def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M:
        if air[nx][ny] == 0:
          air[nx][ny] = 2
          q.append((nx, ny))

# 치즈 없애기
def remove(x, y):
  for i in range(N):
    for j in range(M):
      cnt = 0
      if arr[i][j] == 1:
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < N and 0 <= ny < M:
            if air[nx][ny] == 2:
              cnt += 1
        if cnt >= 2:
          arr[i][j] = 0

# 치즈있는지 확인
def find():
  for i in range(N):
    for j in range(M):
      if arr[i][j] == 1:
        return False
  return True

# main
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
time = 0
while True:
  time += 1
  air = copy.deepcopy(arr)
  bfs(0, 0)
  remove(0, 0)
  if find():
    break
print(time)