# 3. 카드 놓기(실3)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

n = 1
q = deque()

for i in range(N-1, -1, -1):
  if A[i] == 1:
    q.appendleft(n)
  elif A[i] == 2:
    first = q.popleft()
    q.appendleft(n)
    q.appendleft(first)
  else:
    q.append(n)
  n += 1

print(*q)
