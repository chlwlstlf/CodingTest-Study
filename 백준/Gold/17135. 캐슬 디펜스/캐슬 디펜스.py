# 캐슬 디펜스 (골3)

from copy import deepcopy
import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0]
dy = [-1, 0, 1]

def bfs(comb):
  temp = deepcopy(arr)
  cnt = 0
  visited = [[0]*M for _ in range(N)]
  for r in range(N-1, -1, -1):
    result = []
    for c in comb:
      q = deque([(r, c, 1)])
      while q:
        x, y, d = q.popleft()
        if temp[x][y] == 1:
          result.append((x, y))
          if visited[x][y] == 0:
            visited[x][y] = 1
            cnt += 1
          break
        if d < D:
          for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
              q.append((nx, ny, d+1))
    for x, y in result:
      temp[x][y] = 0     
  return cnt

answer = 0
combs = combinations([i for i in range(M)], 3)
for comb in combs:
  answer = max(answer, bfs(comb))
print(answer)
