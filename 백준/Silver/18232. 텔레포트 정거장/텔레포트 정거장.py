# 2. 텔레포트 정거장(실2)

from collections import deque
import sys
input = sys.stdin.readline

# 입력, 그래프 만들기
N, M = map(int, input().split())
S, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
  if i > 1:
    graph[i].append(i-1)
  if i < N:
    graph[i].append(i+1)
for i in range(M):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

# bfs
def bfs(v):
  q = deque()
  q.append(v)
  visited[v] = 1
  while q:
    g = q.popleft()
    for i in graph[g]:
      if visited[i] == 0:
        visited[i] = visited[g]+1
        q.append(i)

visited = [0]*(N+1)
bfs(S)
print(visited[E]-1)