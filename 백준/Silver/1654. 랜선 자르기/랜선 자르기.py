# 24.랜선 자르기 (실2)

import sys
input = sys.stdin.readline

K, N = map(int, input().split())
L = [int(input()) for _ in range(K)]

start = 1
end = max(L)
while start <= end :
  mid = (start+end)//2
  cnt = 0
  for i in range(K):
    cnt += L[i]//mid
  if cnt < N :
    end = mid-1
  else :
    start = mid+1
    result = mid
print(result)
