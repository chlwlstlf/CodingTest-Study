# 3. 줄세우기(골4)
# LIS(최장 증가 부분 수열) 알고리즘: 보통 DP를 이용함


import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

dp = [0]*(N)
for i in range(N):
  dp[i] = 1
  for j in range(i):
    if arr[j] < arr[i]:
      dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))