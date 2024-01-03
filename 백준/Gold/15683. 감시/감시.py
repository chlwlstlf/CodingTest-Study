# 3. 감시 (골4)

import sys
from itertools import product
import copy
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상수화하기
direction = [[], 
             [[(0, -1)], [(0, 1)], [(-1, 0)], [(1, 0)]], 
             [[(0, -1), (0, 1)], [(-1, 0), (1, 0)]], 
             [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]], 
             [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]], 
             [[(0, -1), (0, 1), (-1, 0), (1, 0)]]
            ]
combi = [[], [0, 1, 2, 3], [0, 1], [0, 1, 2, 3], [0, 1, 2, 3], [0]]

# cctv 조합 만들기
cctv = []
for i in range(N):
  for j in range(M):
    if 1 <= arr[i][j] <= 5:
      cctv.append(combi[arr[i][j]])
combinations = list(product(*cctv))

# 최솟값 찾기
def changeArr(array, com):
  cnt = 0
  for i in range(N):
    for j in range(M):
      if 1 <= arr[i][j] <= 5:
        dir = direction[arr[i][j]][com[cnt]]
        cnt += 1
        for k in range(len(dir)): # 각 방향으로 모두 #으로 바꿔주기
          nx, ny = i, j
          while True:
            nx += dir[k][0]
            ny += dir[k][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M or array[nx][ny] == 6:
              break
            else:
              if array[nx][ny] == 0:
                array[nx][ny] = '#'
  return sum(row.count(0) for row in array)

min_value = N*M+1
for com in combinations:
  copiedArr = copy.deepcopy(arr)
  result = changeArr(copiedArr, com)
  if min_value > result:
    min_value = result
print(min_value)
