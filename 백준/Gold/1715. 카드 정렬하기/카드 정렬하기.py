# 4. 카드 정렬하기 (골4)

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
  heappush(h, int(input()))

if N == 1:
  print(0)
  sys.exit()

result = 0
for i in range(N-1):
  a = heappop(h)
  b = heappop(h)
  result += a+b
  heappush(h, a+b)

print(result)