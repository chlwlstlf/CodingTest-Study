# 통나무 건너뛰기 (실1)

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
  N = int(input())
  L = list(map(int, input().split()))
  L.sort()
  answer = 0
  for i in range(2, N):
    answer = max(answer, L[i]-L[i-2])
  print(answer)
