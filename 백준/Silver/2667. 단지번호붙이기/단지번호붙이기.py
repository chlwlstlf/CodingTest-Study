# 2. 단지번호붙이기 (실1)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]

# dfs(1의 개수를 세면서 0으로 바꿔줌)
def dfs(x, y):
  global cnt
  arr[x][y] = 0
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]
    if 0 <= nx < N and 0 <= ny < N:
      if arr[nx][ny] == 1:
        arr[nx][ny] = 0
        cnt += 1
        dfs(nx, ny)
  return cnt

# dfs 반복해서 호출
answer = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
  for j in range(N):
    if arr[i][j] == 1:
      cnt = 1
      dfs(i, j)
      answer.append(cnt)

# 출력
answer.sort()
print(len(answer))
[print(a) for a in answer]