# 시간 관리하기 (골5)

import sys
input = sys.stdin.readline
import heapq
INF = sys.maxsize

N = int(input())
h = []
for i in range(N):
  T, S = map(int, input().split())
  heapq.heappush(h, (-S, -T))

def solve():
  answer = -h[0][0]
  while h:
    s, t = heapq.heappop(h)
    t = -t
    s = -s
    minV = min(answer, s)
    if minV-t >= 0:
      answer = minV-t
    else:
      return -1
  return answer

print(solve())