# 3. 게리맨더링 (골4)

import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

# 입력
N = int(input())
W = list(map(int, input().split()))
W.insert(0, 0)
graph = [[] for _ in range(N+1)]
for i in range(1, N+1):
  arr = list(map(int, input().split()))
  for j in range(1, arr[0]+1):
    graph[i].append(arr[j])

# bfs
def bfs(group):
  q = deque()
  q.append(group[0])
  visited[group[0]] = 1
  while q:
    v = q.popleft()
    for i in graph[v]:
      if visited[i] == 0 and i in group:
        visited[i] = 1
        q.append(i)

arr = [i+1 for i in range(N)]
total = sum(W)
answer = total
for i in range(N//2):
  for c1 in combinations(arr, i+1):
    # c2 만들기
    c2 = []
    result = 0
    for a in arr:
      if a not in c1:
        c2.append(a)
        result += W[a]
    # bfs 호출
    visited = [0]*(N+1)
    bfs(c1)
    bfs(c2)
    if visited.count(0) == 1:
      answer = min(answer, abs((total-result)-result))

if answer == total:
  print(-1)
else:
  print(answer)