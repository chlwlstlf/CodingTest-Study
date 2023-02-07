# 4. 촌수계산(실3)

import sys
input = sys.stdin.readline

#입력
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
arr = [list(map(int, input().split())) for _ in range(m)]

#그래프 생성
graph = [[] for _ in range(n+1)]
for i in range(m):
  graph[arr[i][0]].append(arr[i][1])
  graph[arr[i][1]].append(arr[i][0])

#dfs
def dfs(v, cnt):
  visited[v] = 1
  if v == p2:
    print(cnt)
    return

  for i in graph[v]:
    if not visited[i]:
      dfs(i, cnt+1)

#dfs함수 부르기
visited = [0]*(n+1)
dfs(p1, 0)
if not visited[p2] :
  print(-1)