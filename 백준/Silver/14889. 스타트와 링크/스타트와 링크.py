# 22.스타트와 링크 (실2)

import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
T = [list(map(int, input().split())) for _ in range(N)]

idx = [i for i in range(N)]

result = sys.maxsize
for s in list(combinations(idx, N//2)) :
  start = 0
  link = 0
  l = list(set(idx) - set(s))
  for i, j in list(combinations(s, 2)) :
    start += T[i][j] + T[j][i]
  for i, j in list(combinations(l, 2)) :
    link += T[i][j] + T[j][i]
  result = min(result, abs(start-link))

print(result)
