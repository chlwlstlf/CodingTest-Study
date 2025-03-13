# 카드 구매하기 2 (실1)

import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
arr = list(map(int, input().split()))

dp = [INF]*(N+1)
dp[0] = 0
for i in range(1, N+1):
  dp[i] = arr[i-1]
  for j in range(i//2+1):
    dp[i] = min(dp[j]+dp[i-j], dp[i])

print(dp[N])