# 1. 운동 (골4)

import sys
input = sys.stdin.readline

# 입력, 그래프 만들기
V, E = map(int, input().split())
graph = [[sys.maxsize for _ in range(V)] for _ in range(V)]
for i in range(E):
  a, b, c = map(int, input().split())
  graph[a-1][b-1] = c

# 플로이드-워셜
for i in range(V):
  for j in range(V):
    for k in range(V):
      graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k]) #j에서 k로 바로 가는 것 vs i를 거쳐 가는 것

# 출력
answer = sys.maxsize
for i in range(V):
  answer = min(answer, graph[i][i])

if answer == sys.maxsize:
  print(-1)
else:
  print(answer)