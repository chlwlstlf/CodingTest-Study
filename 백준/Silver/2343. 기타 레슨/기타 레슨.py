# 33. 기타 레슨 (실1)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = list(map(int, input().split()))

start = max(L)
end = sum(L)

while start <= end :
  mid = (start+end)//2

  # mid값에 따른 그룹 수 구하기
  cnt = 1
  total = 0
  for i in L :
    total += i
    if total > mid:
      cnt += 1
      total = i

  # 그룹 수가 M보다 작거나 같을 때 mid값을 result로 갱신
  if cnt > M :
    start = mid+1
  else :
    end = mid-1
    result = mid

print(result)

    