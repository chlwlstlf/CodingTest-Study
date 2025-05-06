# 색종이와 가위 (골5)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

start = 0
end = (n+1)//2
while start <= end:
  mid = (start+end)//2
  h, v = mid, n-mid
  result = (h+1)*(v+1)
  if result < k:
    start = mid+1
  elif result > k:
    end = mid-1
  else:
    print("YES")
    exit()

print("NO")