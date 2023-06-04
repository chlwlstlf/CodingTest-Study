# 7. 달팽이(실3)

import sys
input = sys.stdin.readline

N = int(input())
num = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

d = -1
start = N*N # (0, 0)부터 시작이므로
length = N
x = -1
y = 0
for i in range((N-1)*2+1):
  if i%2 == 0: #i가 짝수 일때는 방향을 바꾸고, 위 또는 아래로 움직임
    d = -d
    for j in range(length):
      x += d
      arr[x][y] = start
      start -= 1
  else: #i가 홀수 일때는 길이가 하나 줄고, 왼쪽 또는 오른쪽으로 움직임
    length -= 1
    for j in range(length):
      y += d
      arr[x][y] = start
      start -= 1

# 출력
for i in range(N):
  print(*arr[i])
  if num in arr[i]:
    target_row = i+1
    target_col = arr[i].index(num) + 1
print(target_row, target_col)
