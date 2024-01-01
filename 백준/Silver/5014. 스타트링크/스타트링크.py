# 4. 스타트링크 (실1)

import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

# bfs
visited = [0]*(F+1)
q = deque()
q.append(S)
visited[S] = 1
while q:
  v = q.popleft()
  if v+U <= F and visited[v+U] == 0:
    visited[v+U] = visited[v] + 1
    q.append(v+U)
  if v-D > 0 and visited[v-D] == 0:
    visited[v-D] = visited[v] + 1
    q.append(v-D)

# 출력
if visited[G] == 0:
  print('use the stairs')
else:
  print(visited[G]-1)
