# 4. 거짓말 (골4)

import sys
input = sys.stdin.readline

# 입력, 그래프 만들기
N, M = map(int, input().split())
T = list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
arr = []
for i in range(M):
  a = list(map(int, input().split()))
  arr.append(a)
  for j in range(1, a[0]+1):
    for k in range(j+1, a[0]+1):
      if a[j] not in graph[a[k]]:
        graph[a[j]].append(a[k])
        graph[a[k]].append(a[j])

# 0일 때
if T[0] == 0:
  print(M)
  sys.exit()

# 0이 아닐 때
# dfs 함수
def dfs(v):
  visited[v] = 1
  for i in graph[v]:
    if visited[i] == 0:
      dfs(i)

# 진실 아는 사람은 visited가 1
visited = [0]*(N+1)
for i in range(T[0]):
  dfs(T[i+1])

# 출력
result = M
for i in range(M):
  for j in range(arr[i][0]):
    if visited[arr[i][j+1]] == 1:
      result -= 1
      break
print(result)