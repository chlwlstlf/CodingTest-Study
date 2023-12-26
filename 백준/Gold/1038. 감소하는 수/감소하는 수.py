# 2. 감소하는 수 (골5)

import sys
import copy
input = sys.stdin.readline

N = int(input())
cnt = 0
arr = [0]
init = [0]

if N > 1022:
  print(-1)
  exit()

def isAdd():
  for i in range(len(arr)-1):
    if arr[i] < arr[i+1]-1:
      arr[i] += 1
      for j in range(i):
        arr[j] = j
      return True
  if arr[-1] < 9:
    arr[-1] += 1
    for i in range(len(arr)-1):
      arr[i] = i
    return True
  return False

while True:
  if cnt == N:
    break
  if not isAdd():
    init.append(len(init))
    arr = copy.deepcopy(init)
  cnt += 1

arr.reverse()
[print(arr[i], end='') for i in range(len(arr))]