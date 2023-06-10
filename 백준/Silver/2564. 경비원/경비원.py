# 2. 경비원(실1)

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
S = int(input())
loc = [list(map(int, input().split())) for _ in range(S+1)]

arr = [0]*(S+1)
for i in range(S+1):
  if loc[i][0] == 1:
    arr[i] = loc[i][1]
  elif loc[i][0] == 2:
    arr[i] = M+N+(M-loc[i][1])
  elif loc[i][0] == 3:
    arr[i] = M+N+M+(N-loc[i][1])
  else:
    arr[i] = M+loc[i][1]

result = 0
for i in range(S):
  length = abs(arr[-1]-arr[i])
  result += min(length, (M+N)*2-length)
print(result)