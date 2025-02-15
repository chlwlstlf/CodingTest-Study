# 트리의 지름 (골2)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

V = int(input())
graph = [[] for _ in range(V+1)]
for i in range(V):
  arr = list(map(int, input().split()))
  for j in range(1, len(arr)-1, 2):
    graph[arr[0]].append((arr[j], arr[j+1]))

def dfs(v, depth):
  global node
  if depth > answer[-1]:
    answer.append(depth)
    node = v
  if visited[v] == 1:
    return
  visited[v] =1
  for i in graph[v]:
    e, w = i
    if visited[e] == 0:
      dfs(e, depth+w)

node = 0
answer = [0]
visited = [0]*(V+1)
dfs(1, 0)

visited = [0]*(V+1)
dfs(node, 0)

print(answer[-1])