# 4. 색종이 올려 놓기 (골4)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 정렬
[arr[i].sort() for i in range(N)]
arr.sort()

# dp
dp = [0]*N
dp[0] = 1
for i in range(1, N):
  m = 1
  for j in range(i):
    if arr[j][0] <= arr[i][0] and arr[j][1] <= arr[i][1]:
      m = max(m, dp[j]+1)
  dp[i] = m
print(max(dp))