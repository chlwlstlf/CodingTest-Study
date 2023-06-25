# 3. 트리의 부모 찾기(실2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000000)

# 입력, 그래프 만들기
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)


def dfs(v):
  if visited[v]:
    return
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      root[i] = v
      dfs(i)



visited = [0]*(N+1)
root = [0]*(N+1)
dfs(1)

for i in range(2, N+1):
  print(root[i])