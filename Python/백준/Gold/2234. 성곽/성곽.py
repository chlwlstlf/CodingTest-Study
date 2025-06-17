# 성곽 (골3)

import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

# 방향 3차원 배열 만들기
graph = [[[0]*4 for _ in range(M)] for _ in range(N)]
for i in range(N):
  for j in range(M):
    v = arr[i][j]
    for k in range(4):
      if v & (1 << k):
        graph[i][j][k] = 1

# 덩어리 번호와 합 구하기
def dfs(x, y, idx):
  if x < 0 or x >= N or y < 0 or y >= M:
    return False
  if total[x][y] == 0:
    total[x][y] = idx
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < N and 0 <= ny < M and graph[x][y][i] == 0:
        dfs(nx, ny, idx)
    return True
  return False

total = [[0]*M for _ in range(N)]
idx = 1
for i in range(N):
  for j in range(M):
    if dfs(i, j, idx) == True:
      idx += 1

# 벽 각 덩어리의 개수 세기
result = [0]*(idx+1)
for i in range(N):
  for j in range(M):
    result[total[i][j]] += 1

# 최댓값 찾기
answer = 0
for i in range(N):
  for j in range(M):
    for k in range(4):
      nx = i + dx[k]
      ny = j + dy[k]
      if 0 <= nx < N and 0 <= ny < M:
        if total[i][j] != total[nx][ny]:
          answer = max(answer, result[total[i][j]]+result[total[nx][ny]])

print(idx-1)
print(max(result))
print(answer)