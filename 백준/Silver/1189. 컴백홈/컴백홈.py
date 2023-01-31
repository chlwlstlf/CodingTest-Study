# 31. 컴백홈 (실1)

import sys
input = sys.stdin.readline

R, C, K = map(int, input().split())
M = [input().rstrip() for _ in range(R)]

visited = [[0]*C for _ in range(R)]
visited[R-1][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, cnt):
  global result
  if x == 0 and y == C-1 :
    if cnt == K:
      result += 1
    return 
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < R and 0 <= ny < C and M[nx][ny] != 'T' and visited[nx][ny] == 0:
      visited[nx][ny] = 1
      dfs(nx, ny, cnt+1)
      visited[nx][ny] = 0

result = 0
dfs(R-1, 0, 1)
print(result)
