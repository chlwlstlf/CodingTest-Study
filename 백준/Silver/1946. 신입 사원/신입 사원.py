# 26. 신입사원(실1) 시간초과

import sys
input = sys.stdin.readline

T = int(input())
R = ""

for i in range (T) :
  p = []
  N = int(input())
  for j in range (N) :
    p.append(list(map(int, input().split())))
  p.sort()

  result = 1
  m = p[0][1]
  for j in range(1, N) :
    if m > p[j][1] :
      m = p[j][1]
      result += 1
      
  R += (str(result) + '\n')

print(R)

 
