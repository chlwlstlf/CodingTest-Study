# 2. A와 B(골5)

import sys
input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

for i in range(len(T)-len(S)):
  if T[-1] == 'A':
    T.pop()
  else:
    T.pop()
    T.reverse()

if S == T:
  print(1)
else:
  print(0)