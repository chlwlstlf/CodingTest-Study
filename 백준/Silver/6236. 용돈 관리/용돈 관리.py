# 23.용돈 관리 (실2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
B = [int(input()) for _ in range(N)]

result = 0
start = max(B)
end = sum(B)
while start <= end :
  mid = (start+end)//2
  cnt = 1
  sum = 0
  for i in range(N):
    sum += B[i]
    if sum > mid :
      cnt += 1
      sum = B[i]
  if cnt > M :
    start = mid+1
  else :
    end = mid-1
    result = mid
print(result)


