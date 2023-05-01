# 1. 눈치우기(실3)

import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

time = 0
a.sort(reverse=True)

while True:
  if len(a) == 0 or len(a) == 1:
    break
  if a[1] == 0:
    a.pop(1)
  if a[0] == 0:
    a.pop(0)
  if len(a) == 0 or len(a) == 1:
    break
  
  a.sort(reverse=True)
  a[0] -= 1
  a[1] -= 1
  time += 1

if len(a) > 0:
  time += a[0]

if time > 1440:
  print(-1)
else:
  print(time)