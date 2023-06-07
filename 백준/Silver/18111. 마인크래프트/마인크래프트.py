# 8. 마인크래프트(실2) 풀어야함

import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

height = [0]*257
for i in range(N):
  for j in range(M):
    height[arr[i][j]] += 1

mn = min([min(arr[i]) for i in range(N)])
mx = max([max(arr[i]) for i in range(N)])
result = [100000000000, mn]
for i in range(mn, mx+1):
  time = 0
  inven = B
  for j in range(mn, mx+1):
    if j > i:
      time += (j-i)*height[j]*2
      inven += (j-i)*height[j]
    elif j < i:
      time += (i-j)*height[j]
      inven -= (i-j)*height[j]
  if inven < 0 or result[0] < time:
    break
  result = [time, i]


print(*result)