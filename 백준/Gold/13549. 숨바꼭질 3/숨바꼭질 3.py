# 1. 숨바꼭질 3 (골5)

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [-1] *100001

# bfs
q = deque()
q.append(N)
arr[N] = 0
while q:
  v = q.popleft()
  if v*2 <= 100000 and arr[v*2] == -1:
    arr[v*2] = arr[v]
    q.append(v*2)
  if v-1 >= 0 and arr[v-1] == -1:
    arr[v-1] = arr[v]+1
    q.append(v-1)
  if v+1 <= 100000 and arr[v+1] == -1:
    arr[v+1] = arr[v]+1
    q.append(v+1)
  if arr[K] != -1:
    print(arr[K])
    break