# 1. 맥주 마시면서 걸어가기(골5)

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
  #입력
  n = int(input())
  arr = [list(map(int, input().split())) for _ in range(n+2)]
  #그래프 만들기
  graph = [[] for _ in range(n+2)]
  for i in range(n+2):
    for j in range(i+1, n+2):
      if abs(arr[i][0]-arr[j][0]) + abs(arr[i][1]-arr[j][1]) <= 1000:
        graph[i].append(j)
        graph[j].append(i)
  #bfs
  visited = [0]*(n+2)
  q = deque([0])
  visited[0] = 1
  while q:
    v = q.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        visited[i] = 1
        q.append(i)
  #출력
  if visited[-1] == 1: print("happy")
  else: print("sad")
