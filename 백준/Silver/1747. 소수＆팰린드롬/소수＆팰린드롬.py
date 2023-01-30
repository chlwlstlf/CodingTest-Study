# 35. 소수&팰린드롬 (실1)

import sys
input = sys.stdin.readline

N = int(input())

while True:
  n = list(map(int, str(N)))

  #팰린드롬 검사
  f1 = 0
  for i in range(len(n)//2):
    if n[i] != n[len(n)-i-1]:
      f1 = 1
      break
  
  #팰린드롬 수일 때 소수 검사
  f2 = 1
  if f1 == 0:
    if N == 1:
      print(2)
      break
    f2 = 0
    for i in range (2, N):
      if N % i == 0:
        f2 = 1
        break
  
  if f2 == 0:
    print(N)
    break

  N += 1