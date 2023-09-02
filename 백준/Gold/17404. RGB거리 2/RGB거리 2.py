# 4. RGB거리 2(골4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = []

for i in range(3):
  dp = [[sys.maxsize for _ in range(3)] for _ in range(N+1)]
  dp[1][i] = arr[0][i]
  for j in range(2, N+1):
    dp[j][0] = min(dp[j-1][1], dp[j-1][2])+arr[j-1][0]
    dp[j][1] = min(dp[j-1][0], dp[j-1][2])+arr[j-1][1]
    dp[j][2] = min(dp[j-1][0], dp[j-1][1])+arr[j-1][2]
  for j in range(3):
    if i != j:
      ans.append(dp[N][j])

print(min(ans))