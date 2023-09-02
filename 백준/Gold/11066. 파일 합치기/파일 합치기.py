# 2. 파일 합치기(골3)
# 연속된 파일이므로 heap이 아닌 dp로 풀어야함
'''
dp[2][3]은 2와 3을 합친 값
dp[1][4]는 dp[1][1]+dp[2][4], dp[1][2]+dp[3][4], dp[1][3]+dp[4][4] 중 최솟값

dp[i][j] = dp[i][j-1] + arr[j] + min(minimum)

<크누스 최적화>
첫 번째 for문 이후
0  70 100 150
0   0  60 110
0   0   0  80
0   0   0   0

두 번째 for문 이후
0  70 160 300
0   0  60 170
0   0   0  80
0   0   0   0
'''

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
  K = int(input())
  arr = list(map(int, input().split()))
  dp = [[0 for _ in range(K)] for _ in range(K)]
  
  for i in range(K-1):
    dp[i][i+1] = arr[i] + arr[i+1]
    for j in range(i+2, K):
      dp[i][j] = dp[i][j-1] + arr[j]

  for i in range(2, K):
    for j in range(K-i):
      t = i+j
      mn = sys.maxsize
      for k in range(j, t):
        mn = min(mn, dp[j][k] + dp[k+1][t])
      dp[j][t] += mn

  print(dp[0][K-1])
  