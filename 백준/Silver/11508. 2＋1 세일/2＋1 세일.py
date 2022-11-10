# 35. 2+1 세일 (실4)

import sys
input = sys.stdin.readline

N = int(input())
C = [int(input()) for _ in range(N)]

C.sort(reverse=True)

result = 0
if len(C) < 2 :
  result = sum(C)
else :
  for i in range(N) :
    if i % 3 != 2 :
      result += C[i]

print(result)