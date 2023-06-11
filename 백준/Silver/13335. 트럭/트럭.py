# 1. 트럭(실1)

import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())
a = list(map(int, input().split()))

q = deque()
cnt = deque()
time = 0
i = 0
while True:
  if i == n: #이 조건이 제일 먼저 나와야함
    break
  for j in range(len(cnt)):
    cnt[j] -= 1
  if cnt and cnt[0] == 0:
    q.popleft()
    cnt.popleft()
  if len(q) == 0 or sum(q)+a[i] <= L:
    q.append(a[i])
    cnt.append(w)  
    i += 1
  time += 1
  
time += cnt[-1]
print(time)