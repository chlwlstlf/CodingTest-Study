# 9. 암기왕 (실4)

import sys
from bisect import bisect_left, bisect_right
# input = sys.stdin.readline


T = int(input())
for i in range (T):
  #입력
  N = int(input())
  note1 = list(map(int, input().split()))
  M = int(input())
  note2 = list(map(int, input().split()))


  note1.sort()

  for j in range (M):
    if bisect_right(note1, note2[j])-bisect_left(note1, note2[j])>0:
      print(1)
    else :
      print(0)