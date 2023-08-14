import sys
import copy
from collections import deque
input = sys.stdin.readline

# 입력 & 초기 arr 그리기
N, M, K = map(int, input().split())
arr = [[deque() for _ in range(N)] for _ in range(N)]
ball = deque()
for i in range(M):
  r, c, m, s, d = list(map(int, input().split()))
  ball.append((r, c, m, s, d))

# 1. 파이어볼 이동
def move(r, c, m, s, d):
  nr = (r + s*dr[d]) % N
  nc = (c + s*dc[d]) % N
  arr[nr][nc].append((m, s, d))

# 2. 파이어볼 나눠짐
def divide(r, c, q):
  n, m_total, s_total, odd, even = len(q), 0, 0, 0, 0
  while q:
    m, s, d = q.popleft()
    m_total += m 
    s_total += s
    if d%2 == 0:
      even += 1
    else:
      odd += 1

  rm = m_total//5
  rs = s_total//n
  if rm > 0:
    if even == n or odd == n:
      for i in range(0, 8, 2):
        ball.append((r, c, rm, rs, i))
    else:
      for i in range(1, 8, 2):
        ball.append((r, c, rm, rs, i))

# K번 명령
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(K):
  # 1. 파이어볼 이동
  while ball:
    r, c, m, s, d = ball.popleft()
    move(r, c, m, s, d)
  # 2. 2개 이상인 곳 파이어볼 나눠짐
  for j in range(N):
    for k in range(N):
      if len(arr[j][k]) >= 2:
        divide(j, k, arr[j][k])
      if len(arr[j][k]) == 1:
        ball.append((j, k) + arr[j][k].pop())

# 출력
print(sum(b[2] for b in ball))