# 11. 외판원 순회2(실2)

import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(N):
    if W[i][j] != 0:
      graph[i].append(j)

def dfs(v, s):
  if visited.count(1) == N:
    if W[v][0]:
      result.append(s+W[v][0])
    return
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      visited[i] = 1
      dfs(i, s+W[v][i])
      visited[i] = 0

result = []
visited = [0]*N
dfs(0, 0)
print(min(result))