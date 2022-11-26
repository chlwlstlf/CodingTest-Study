# 5. 유레카 이론 (브1) 시간초과

import sys
input = sys.stdin.readline

def isEureka(n):
  for i in range (1, n):
    for j in range (i, n-i):
      k = n-i-j
      if i in Tri and j in Tri and k in Tri:
        return 1
  return 0

#삼각수 배열
Tri = [i*(i+1)/2 for i in range(1, 46)]

#입력
T = int(input())
for i in range (T):
  print(isEureka(int(input())))
