# 20.부분수열의 합 (실2) 못 풀겠음

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

cnt = 0
def bt(idx, total):
  global cnt
  if idx == N :
    if total == S :
      cnt += 1
    return
  bt(idx+1, total)
  bt(idx+1, total+array[idx])

bt(0, 0)
if S == 0:
  cnt -=1

print(cnt)
