# 가장 긴 바이토닉 부분 수열 (골4)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp1 = [1]*N
for i in range(N):
  for j in range(i):
    if arr[i] > arr[j]:
      dp1[i] = max(dp1[i], dp1[j]+1)

dp2 = [1]*N
for i in range(N-1, -1, -1):
  for j in range(N-1, i, -1):
    if arr[i] > arr[j]:
      dp2[i] = max(dp2[i], dp2[j]+1)

answer = 0
for i in range(N):
  answer = max(answer, dp1[i]+dp2[i]-1)
print(answer)
