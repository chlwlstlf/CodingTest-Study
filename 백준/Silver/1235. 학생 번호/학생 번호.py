# 학생 번호 (실4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

M = len(str(arr[0]))

for i in range(1, M+1):
  result = set()
  for j in range(N):
    result.add(arr[j]%(10**i))
  if len(result) == N:
    print(i)
    break