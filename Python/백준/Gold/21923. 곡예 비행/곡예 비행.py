# 곡예 비행 (골4)

import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

def solve():
  # 상승 dp
  dp1 = [[-INF]*M for _ in range(N)]
  dp1[N-1][0] = arr[N-1][0]

  for i in range(N-1, -1, -1):
    for j in range(M):
      if i < N-1:
        dp1[i][j] = max(dp1[i][j], dp1[i+1][j]+arr[i][j])
      if j > 0:
        dp1[i][j] = max(dp1[i][j], dp1[i][j-1]+arr[i][j])

  # 하강 dp
  dp2 = [[-INF]*M for _ in range(N)]
  dp2[N-1][M-1] = arr[N-1][M-1]

  for i in range(N-1, -1, -1):
    for j in range(M-1, -1, -1):
      if i < N-1:
        dp2[i][j] = max(dp2[i][j], dp2[i+1][j]+arr[i][j])
      if j < M-1:
        dp2[i][j] = max(dp2[i][j], dp2[i][j+1]+arr[i][j])

  # 합 제일 큰 곳 구하기
  answer = -INF
  for i in range(N):
    for j in range(M):
      answer = max(answer, dp1[i][j]+dp2[i][j])
  return answer

print(solve())