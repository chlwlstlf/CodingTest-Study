# 춘배가 선물하는 특별한 하트 (골5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

def solve():
  num = [N]
  if N == M:
    return "YES"
  while num:
    s = set()
    for n in num:
      if n == 1:
        continue
      if n%2 == 0:
        s.add(n//2)
      else:
        s.add((n-1)//2)
        s.add((n-1)//2+1)
    if M in s:
      return "YES"
    num = list(s)
  return "NO"

print(solve())