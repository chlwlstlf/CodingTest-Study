# 3. 바이러스(실3)

import sys
input = sys.stdin.readline

#입력
N = int(input())
E = int(input())
arr = [list(map(int, input().split())) for _ in range(E)]

#그래프 생성
graph = [[] for i in range(N+1)]
for i in range(E):
  graph[arr[i][0]].append(arr[i][1])
  graph[arr[i][1]].append(arr[i][0])

#dfs
def dfs(v, visited):
  visited[v] = 1
  for i in graph[v]:
    if not visited[i]:
      dfs(i, visited)

#dfs함수 부르고 출력
visited = [0]*(N+1)
dfs(1, visited)
print(visited.count(1)-1)