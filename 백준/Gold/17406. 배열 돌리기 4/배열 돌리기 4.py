# 2. 배열 돌리기 4 (골4)

import sys
import copy
input = sys.stdin.readline

# 입력
N, M, K = map(int, input().split())
A = []
for i in range(N):
  A.append(list(map(int, input().split())))
O = []
for i in range(K):
  O.append(list(map(int, input().split())))

# 계산
def dfs(arr, v, cnt):
  visited[v] = 1
  r, c, s = O[v][0]-1, O[v][1]-1, O[v][2]

  for i in range(s, 0, -1):
    tmp = arr[r-i][c-i]
    # 1. 왼 / 위로 한 칸씩
    for j in range(r-i+1, r+i+1):
      arr[j-1][c-i] = arr[j][c-i]
    # 2. 아래 / 왼쪽으로 한 칸씩
    for j in range(c-i+1, c+i+1):
      arr[r+i][j-1] = arr[r+i][j]
    # 3. 오 / 아래로 한 칸씩
    for j in range(r+i-1, r-i-1, -1):
      arr[j+1][c+i] = arr[j][c+i]
    # 4. 위 / 오른쪽으로 한 칸씩
    for j in range(c+i-1, c-i, -1):
      arr[r-i][j+1] = arr[r-i][j]   
    arr[r-i][c-i+1] = tmp
  
  m = 9999999
  if cnt+1 == K:
    for i in arr:
      m = min(m, sum(i))
    result.append(m)
    return

  for i in range(K):
    if visited[i] == 0:
      visited[i] = 1
      ar = copy.deepcopy(arr)
      dfs(ar, i, cnt+1)
      visited[i] = 0


result = []
for i in range(K):
  visited = [0]*K
  a = copy.deepcopy(A)
  dfs(a, i, 0)
print(min(result))