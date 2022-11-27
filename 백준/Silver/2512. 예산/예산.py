# 17. 예산 (실3)

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))
budget = int(input())

start = 0
end = max(X)

result = 0
while (start <= end) :
  total = 0
  mid = (start+end)//2
  for x in X:
    if x > mid : #mid값보다 크다면 mid값을 더해주고
      total += mid
    else : #mid값보다 작다면 원래값 더해줌
      total += x
  if total <= budget: #예산보다 적으면
    result = mid #result값 갱신해주고
    start = mid+1 #mid값을 늘려나감
  else:
    end = mid-1 #예산보다 크면 mid 줄임

print(result)