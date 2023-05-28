# 2. 회전하는큐 (실3)

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

result = 0
start = 0
arr = [i+1 for i in range(N)]

for i in range(M):
  idx = arr.index(a[i])
  result += min(abs(idx-start), len(arr)-abs(idx-start))
  if idx == len(arr)-1:
    start = 0
  else:
    start = idx
  arr.pop(idx)
print(result)