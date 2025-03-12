# Router (실4)

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
q = deque()

while True:
  a = int(input())
  if a == -1:
    break
  if a == 0:
    q.popleft()
  else:
    if len(q) < N:
      q.append(a)

print(*q)