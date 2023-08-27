# 1. 가운데를 말해요(골2)
# 작은 거는 최대힙
# 큰 거는 최소힙

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N = int(input())
maxheap = [] #중간 값보다 작은 수
minheap = [] #중간 값보다 큰 수

if N == 1:
  x = int(input())
  print(x)
  sys.exit()

x1 = int(input())
print(x1)
x2 = int(input())
if x1 < x2:
  heappush(maxheap, -x1)
  heappush(minheap, x2)
  print(x1)
else:
  heappush(maxheap, -x2)
  heappush(minheap, x1)
  print(x2)
for i in range(3, N+1):
  x = int(input())
  if minheap[0] > x:
    heappush(maxheap, -x)
  else:
    heappush(minheap, x)
  # 개수 맞추기
  if len(minheap) < i//2:
    heappush(minheap, -heappop(maxheap))
  if len(minheap) > i//2:
    heappush(maxheap, -heappop(minheap))
  print(-maxheap[0])
  
