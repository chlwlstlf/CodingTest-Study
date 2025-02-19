# 게임 개발 (골3)

import sys
input = sys.stdin.readline

N = int(input())
arr = [[i]+list(map(int, input().split())) for i in range(1, N+1)]

dp = [0]*(N+1)

def find(node, time, array):
  result = 0
  if not array:
    dp[node] = time
    return
  for i in range(len(array)):
    if dp[array[i]] <= 0:
      return
    result = max(result, dp[array[i]]+time)
  dp[node] = result

for i in range(N):
  for a in arr:
    find(a[0], a[1], a[2:-1])

for i in range(N):
  print(dp[arr[i][0]])