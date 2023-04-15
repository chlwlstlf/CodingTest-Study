# 1. 십자카드 문제 (실3)

import sys
input = sys.stdin.readline

num = list(map(int, input().split()))

#시계수 찾는 함수
def time_number(n):
  result = 10000
  n = str(n)
  for i in range(4):
    x = n[i:]+n[:i]
    if int(x) < result:
      result = int(x)
  return result



N = int(''.join(map(str, num)))
N = time_number(N)

i = 1111
cnt = 1
while i < N:
  if '0' not in str(i):
    if i == time_number(i):
      cnt += 1
  i += 1
print(cnt)



