# 환승 (골2)

import sys
input = sys.stdin.readline
from collections import deque

N, K, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  arr = list(map(int, input().split()))
  for j in range(K):
    graph[arr[j]].append(N+i+1)
  graph += [arr]

def bfs(v):
  visited[v] = 1
  q = deque()
  q.append(v)
  while q:
    v = q.popleft()
    if v == N:
      return visited[v]
    for i in graph[v]:
      if visited[i] == 0:
        if i > N:
          visited[i] = visited[v]
        else:
          visited[i] = visited[v]+1
        q.append(i)
  return -1

visited = [0]*(N+M+1)
print(bfs(1))