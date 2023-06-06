# 12. 기차가 어둠을 헤치고 은하수를(실2)

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
T = [deque([0 for _ in range(20)]) for _ in range(N)]
for i in range(M):
  O = list(map(int, input().split()))
  if O[0] == 1:
    if T[O[1]-1][O[2]-1] == 0:
      T[O[1]-1][O[2]-1] = 1
  elif O[0] == 2:
    if T[O[1]-1][O[2]-1] == 1:
      T[O[1]-1][O[2]-1] = 0
  elif O[0] == 3:
    T[O[1]-1].pop()
    T[O[1]-1].appendleft(0)
  else:
    T[O[1]-1].popleft()
    T[O[1]-1].append(0)

result = 0
visited = [0]*N
for i in range(N):
  if visited[i] == 0:
    for j in range(i+1, N):
      if visited[j] == 0:
        if T[i] == T[j]:
          visited[j] = 1
    result += 1
print(result)