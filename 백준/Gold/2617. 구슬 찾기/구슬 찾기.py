# 1. 구슬 찾기 (골4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]
for i in range(M):
  a, b = map(int, input().split())
  graph1[b].append(a)
  graph2[a].append(b)


def dfs(v, graph):
  global cnt
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      cnt += 1
      dfs(i, graph)

result = 0
for i in range(N):
  visited = [0]*(N+1)
  cnt = 0
  dfs(i+1, graph1)
  if cnt > N//2:
    result += 1
  
  visited = [0]*(N+1)
  cnt = 0
  dfs(i+1, graph2)
  if cnt > N//2:
    result += 1
    
print(result)
