# 4. 일곱 난쟁이 (브1)

import sys
input = sys.stdin.readline

height = [int(input()) for _ in range(9)]

s = sum(height)
f = 0
for i in range (9):
  for j in range (i+1, 9):
    if s-height[i]-height[j] == 100:
      height.pop(j)
      height.pop(i)
      f = 1
      break
  if f == 1 :
    break


height.sort()
for i in range (7):
  print(height[i])