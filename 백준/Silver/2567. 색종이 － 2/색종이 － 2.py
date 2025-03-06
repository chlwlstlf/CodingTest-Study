# 색종이 - 2 (실4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
  x, y = map(int, input().split())
  for i in range(10):
    for j in range(10):
      arr[x+i][y+j] = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0
for i in range(101):
  for j in range(101):
    if arr[i][j] == 1:
      for d in range(4):
        nx = i + dx[d]
        ny = j + dy[d]
        if 0 <= nx < 101 and 0 <= ny < 101 and arr[nx][ny] == 0:
          answer += 1
print(answer)
