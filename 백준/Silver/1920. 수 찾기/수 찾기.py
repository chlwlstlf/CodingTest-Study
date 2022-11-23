# 12. 수찾기 (실4)

import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for i in range (M):
  if bisect_right(A, B[i])-bisect_left(A, B[i])>0: 
    print(1)
  else :
    print(0)
