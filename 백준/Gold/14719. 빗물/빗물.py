# 1. 빗물(골5)

import sys
input = sys.stdin.readline

H, W = map(int, input().split())
height = list(map(int, input().split()))

# 그림처럼 배열 만들기
arr = []
for i in range(H, 0, -1):
  a = []
  for j in range(W):
    if height[j] >= i:
      a.append(1)
    else:
      a.append(0)
  arr.append(a)    

result = 0
for i in range(H):
  f = 0
  r = 0
  for j in range(W):
    if arr[i][j] == 1:
      f = 1
      result += r
      r = 0
    if arr[i][j] == 0 and f == 1:
      r += 1
print(result)
