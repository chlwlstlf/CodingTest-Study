# 6. 영화감독 숌 (실5)

import sys
input = sys.stdin.readline

N = int(input())

cnt = 0
n = 665
while True :
  while True :
    n += 1
    if '666' in str(n) :
      cnt += 1
      result = n
      break
  if cnt == N :
    break
print(result)
