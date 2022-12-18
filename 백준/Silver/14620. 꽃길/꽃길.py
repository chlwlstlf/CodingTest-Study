# 21. 꽃길 (실2) 못풀겠음

import sys
input = sys.stdin.readline

N = int(input())
G = [list(map(int, input().split())) for _ in range(N)]

def isVisited(r, c):
  f[r-1][c], f[r+1][c], f[r][c-1], f[r][c+1], f[r][c] = 1, 1, 1, 1, 1
  total = G[r-1][c] + G[r+1][c] + G[r][c-1] + G[r][c+1] + G[r][c]
  return total

n = (N-2)*(N-2)
r = []

for i in range (0, n-2):
  for j in range (i+1, n-1):
    for k in range (j+1, n):
      f = [[0]*N for _ in range(N)]
      result = 0
      result += isVisited(i//(N-2)+1, i%(N-2)+1)
      result += isVisited(j//(N-2)+1, j%(N-2)+1)
      result += isVisited(k//(N-2)+1, k%(N-2)+1)
      cnt = 0
      for l in range (N):
        cnt += f[l].count(1)
      if cnt == 15:
        r.append(result)

print(min(r))

    