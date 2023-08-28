# 3. 플로이드(골4)

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[sys.maxsize for _ in range(n)] for _ in range(n)]

for i in range(m):
  a, b, c = map(int, input().split())
  arr[a-1][b-1] = min(arr[a-1][b-1], c)
for i in range(n):
  arr[i][i] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      arr[i-1][j-1] = min(arr[i-1][j-1], arr[i-1][k-1]+arr[k-1][j-1])

for i in range(n):
  for j in range(n):
    if arr[i][j] == sys.maxsize:
      arr[i][j] = 0

for i in arr:
  print(*i)