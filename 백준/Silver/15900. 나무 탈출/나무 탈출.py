# 3. 나무 탈출 (실1)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 입력 후 그래프 그리기
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

# dfs
def dfs(v, depth):
  global result
  visited[v] = 1
  if len(graph[v]) == 1 and visited[graph[v][0]]: # 리프노드인지 확인
    result += depth-1
    return
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i, depth+1)

# dfs 호출
visited = [0]*(N+1)
result = 0
dfs(1, 1)

# 출력
if result%2 == 1:
  print("Yes")
else:
  print("No")
