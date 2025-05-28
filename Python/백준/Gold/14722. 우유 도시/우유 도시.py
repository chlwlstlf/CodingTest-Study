# 우유 도시 (골4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
for i in range(N):
  for j in range(N):
    if i > 0:
      dp[i][j] = max(dp[i][j], dp[i-1][j])
    if j > 0:
      dp[i][j] = max(dp[i][j], dp[i][j-1])
    if arr[i][j] == dp[i][j] % 3:
      dp[i][j] += 1

print(dp[-1][-1])