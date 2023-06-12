# 3. 배열 돌리기 1(실1)

import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 배열에 하나씩 넣기
# arr: [deque([1, 5, 9, 13, 14, 15, 16, 12, 8, 4, 3, 2]), deque([6, 10, 11, 7])]
d = -1
length = cnt = i = 0
x = -1
y = 0
arr = []
q = deque()
while True:
  if i%2 == 0:
    d = -d
    for j in range(N-length):
      x += d
      q.append(A[x][y])
      cnt += 1
  else:
    length += 1
    for j in range(M-length):
      y += d
      q.append(A[x][y])
      cnt += 1
  i += 1
  if i%4 == 0:
    arr.append(q)
    q = deque()
  if cnt == (N*M):
    break
if q:
  arr.append(q)

# 반시계 회전
for i in range(min(M, N)//2):
  arr[i].rotate(R)
  arr[i] = list(arr[i])
arr = sum(arr, []) # 이차원 배열 → 일차원 배열

# 출력
result = [[0 for _ in range(M)] for _ in range(N)]
d = -1
length = cnt = i = 0
x = -1
y = 0
while True:
  if i%2 == 0:
    d = -d
    for j in range(N-length):
      x += d
      result[x][y] = arr[cnt]
      cnt += 1
  else:
    length += 1
    for j in range(M-length):
      y += d
      result[x][y] = arr[cnt]
      cnt += 1
  i += 1
  if cnt == (N*M):
    break
for i in range(N):
  print(*result[i])