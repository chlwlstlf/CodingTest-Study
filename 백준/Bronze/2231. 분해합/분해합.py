# 2. 분해합 (브2) 시간초과

import sys
input = sys.stdin.readline

N = int(input())

l = len(str(N))
n = int('1'+'0'*(l-2))

f = 0
while True :
  if N == n + sum(map(int, str(n))):
    f = 1
    break
  if n > N:
    break
  n += 1

if f == 1 :
  print(n)
else :
  print(0)
