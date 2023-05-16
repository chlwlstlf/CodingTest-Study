# 1. N번째 큰 수 (실2)

import sys
import heapq
input = sys.stdin.readline

N = int(input())

h = []
for i in range(N):
  row = list(map(int, input().split()))
  for j in range(N):
    heapq.heappush(h, row[j])
    if len(h) > N:
      heapq.heappop(h)

print(heapq.heappop(h))