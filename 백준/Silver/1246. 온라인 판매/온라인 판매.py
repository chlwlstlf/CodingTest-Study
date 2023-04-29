# 3. 온라인 판매(실4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = [int(input()) for _ in range(M)]

result = 0
price = 0

for i in range(M-1, -1, -1):
  s = 0
  cnt = 0
  for j in range(M):
    if P[i] <= P[j]:
      s += P[i]
      cnt += 1
    if cnt == N:
      break
  if s > result:
    price = P[i]
    result = s

print(price, result)