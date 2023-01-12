# 28.로또 (실2)

import sys
from itertools import combinations
input = sys.stdin.readline

while True :
  S = list(map(int, input().split()))
  k = S.pop(0)
  
  if k == 0:
    break

  for com in list(combinations(S, 6)):
    print(' '.join(map(str, com)))
  print()
