# 17. 회의실 배정 2(실2)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[0], x[1]))
graph = [[] for _ in range(N)]
for i in range(N):
  for j in range(i+1, N):
    if arr[j][0] >= arr[i][1]:
      graph[i].append([j, arr[j][2]])

def dfs(v):
  global s
  visited[v] = 1
  for i in graph[v]:
    if visited[i[0]] == 0:
      s += i[1]
      visited[i[0]] = 1
      dfs(i[0])
      s -= i[1]
      visited[i[0]] = 0
  result.append(s)

result = []
for i in range(N):
  visited = [0]*N
  s = arr[i][2]
  dfs(i)
print(max(result))