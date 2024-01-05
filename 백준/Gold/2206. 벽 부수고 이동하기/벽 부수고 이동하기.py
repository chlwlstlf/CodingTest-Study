# 5. 벽 부수고 이동하기 (골3)
# 구글 도움

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y, flag):
  q = deque()
  q.append((x, y, flag))
  visited[x][y][flag] = 1
  while q:
    x, y, flag = q.popleft()
    if x == N-1 and y == M-1:
      return visited[x][y][flag]
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx < 0 or nx >= N or ny < 0 or ny >= M:
        continue
      # 벽 안 부수고 이동
      if arr[nx][ny] == 0 and visited[nx][ny][flag] == 0:
        q.append((nx, ny, flag))
        visited[nx][ny][flag] = visited[x][y][flag] + 1
      # 벽 부수고 이동 (처음에 1로 시작해서 부순게 있다면 0으로 간다)
      if arr[nx][ny] == 1 and flag == 1:
        q.append((nx, ny, flag-1))
        visited[nx][ny][flag-1] = visited[x][y][flag] + 1
  return -1

print(bfs(0, 0, 1))
