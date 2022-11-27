# 18. IF문 좀 대신 써줘 (실3)

import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
name = []
value = []
for i in range (N):
  n, v = map(str, input().split())
  name.append(n)
  value.append(int(v))

#이진탐색
for i in range (M):
  power = int(input())
  start = 0
  end = N-1
  while (start <= end):
    mid = (start+end)//2
    if power <= value[mid]:
      result = name[mid]
      end = mid-1
    else :
      start = mid+1     
  print(result)
