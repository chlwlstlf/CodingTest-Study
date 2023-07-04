# 3. 특정 거리의 도시 찾기(실2)

from collections import deque
import sys
input = sys.stdin.readline

# 입력, 그래프 만들기(단방향)
N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
  A, B = map(int, input().split())
  graph[A].append(B)

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

#bfs 호출
visited = [0]*(N+1)
bfs(X)

# 출력
f = 0
for i in range(1, N+1):
  if visited[i]-1 == K:
    print(i)
    f = 1
if f == 0:
  print(-1)