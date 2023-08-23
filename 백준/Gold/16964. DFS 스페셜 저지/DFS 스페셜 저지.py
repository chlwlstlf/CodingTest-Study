# 2. DFS 스페셜 저지 (골 3) 못풀겠음

import sys
from collections import deque
input = sys.stdin.readline

# 입력
N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
order = deque(map(int, input().split()))
# 1부터 탐색하지 않으면 0 출력
if order[0] != 1:
  print(0)
  sys.exit()

def dfs():
  now = order.popleft()
  if not order:
    print(1)
    sys.exit()
  visited[now] = 1
  for i in graph[now]:
    if order[0] in graph[now] and visited[order[0]] == 0:
      dfs()
  return

visited = [0]*(N+1) 
dfs()
print(0)