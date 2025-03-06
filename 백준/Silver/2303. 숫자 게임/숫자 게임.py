# 숫자 게임 (실5)

import sys
input = sys.stdin.readline
from itertools import combinations

answer = [0, 0]
N = int(input())
for i in range(N):
  arr = list(map(int, input().split()))
  combs = combinations(arr, 3)
  maxV = max([sum(comb)%10 for comb in combs])
  if answer[1] <= maxV:
    answer[0] = i+1
    answer[1] = maxV
print(answer[0])