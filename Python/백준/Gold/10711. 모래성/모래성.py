# 모래성 (골2)

import sys
input = sys.stdin.readline
from collections import deque
import copy

H, W = map(int, input().split())
arr = []
for i in range(H):
  a = input().rstrip().replace(".", "0")
  aa = list(map(int, list(a)))
  arr.append(aa)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs():
  # 모래성 주변 무너진 곳 개수 세기
  result = [[0]*W for _ in range(H)]
  q = deque()
  for i in range(1, H-1):
    for j in range(1, W-1):
      if 0 < arr[i][j] < 9:
        for k in range(8):
          nx = i + dx[k]
          ny = j + dy[k]
          if arr[nx][ny] == 0:
            result[i][j] += 1
        if result[i][j] >= arr[i][j]:
          q.append((i, j))

  answer = 0
  visited = [[0]*W for _ in range(H)]
  while q:
    N = len(q)
    # 무너뜨리고 주변 무너진 곳 개수 증가
    for i in range(N):
      x, y = q.popleft()
      visited[x][y] = 1
      arr[x][y] = 0
      for j in range(8):
        nx = x + dx[j]
        ny = y + dy[j]
        result[nx][ny] += 1
        # 새롭게 무너질 곳 찾기
        if 0 < arr[nx][ny] < 9 and result[nx][ny] >= arr[nx][ny] and visited[nx][ny] == 0:
          q.append((nx, ny))
          visited[nx][ny] = 1

    answer += 1

  return answer

print(bfs())