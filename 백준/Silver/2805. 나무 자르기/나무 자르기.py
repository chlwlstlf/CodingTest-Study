# 25.나무 자르기 (실2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
T = list(map(int, input().split()))

start = 0
end = max(T) 
while start <= end :
  mid = (start+end)//2
  total = 0
  for i in range(N):
    if T[i] > mid:
      total += T[i]-mid
  if total < M :
    end = mid-1
  else :
    start = mid+1
    result = mid
  
    
print(result)