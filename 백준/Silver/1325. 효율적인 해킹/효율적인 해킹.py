# 4. 효율적인 해킹 (실1)

import sys
from collections import deque
input = sys.stdin.readline

# 입력, 그래프 만들기
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  graph[b].append(a)

# bfs
def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = 1
  cnt = 0
  while q:
    cnt += 1
    v = q.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = 1
        q.append(i)
  return cnt

# dfs 호출 후 출력
result = [0]*(N+1)
for i in range(1, N+1):
  visited = [0]*(N+1)
  result[i] = bfs(i)

max_value = max(result)
for i in range(1, N+1):
  if max_value == result[i]:
    print(i, end=' ')