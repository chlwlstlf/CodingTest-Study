# 1. 에너지 모으기 (실1)

import sys
import copy
from itertools import permutations
input = sys.stdin.readline

N = int(input())
W = list(map(int, input().split()))

def dfs(arr, result):
  if len(arr) == 2:
    max_value.append(result)
    return
  for i in range(1, len(arr)-1):
    copied_arr = copy.deepcopy(arr)
    r = copied_arr[i-1]*copied_arr[i+1]
    del copied_arr[i]
    dfs(copied_arr, result+r)

max_value = []
dfs(W, 0)
print(max(max_value))