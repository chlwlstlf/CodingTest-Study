# 1. 퇴사(실3)

import sys
input = sys.stdin.readline

N = int(input())
T = [0]*N #소요 날짜
P = [0]*N #수익
for i in range(N):
  T[i], P[i] = map(int, input().split())

R = []  #오늘 날짜+소요 날짜
for i in range(N):
  R.append(T[i]+i)

#dp[i][0]은 상담 했을 때, dp[i][1]은 상담 안 했을 때
dp = [[0 for _ in range(2)] for _ in range(N+6)]

answer = 0
for i in range(1, N+6):
  dp[i][1] = dp[i-1][0]
  answer = dp[i-1][0]
  for j in range(N):
    if R[j] == i:
      answer = max(answer, P[j]+dp[i-T[j]+1][1])
  dp[i][0] = answer
    

print(max(dp[N]))