# 2. 경사로 (골3)

import sys
input = sys.stdin.readline
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# isPass 함수
def isPass(road):
  visited = [0]*N
  for i in range(1, N):
    r = abs(road[i-1]-road[i])
    if r > 1:
      return False
    if r == 1:
      if road[i-1] < road[i]:
        if i-L < 0:
          return False
        if visited[i-L:i] != [0]*L:
          return False
        visited[i-L:i] = [1]*L
      else:
        if i+L > N:
          return False
        if visited[i:i+L] != [0]*L:
          return False
        visited[i:i+L] = [1]*L
  return True


result = 0
for i in range(N):
  result += isPass(arr[i])
  transposed_row = [arr[j][i] for j in range(N)]
  result += isPass(transposed_row)
print(result)