# 붙임성 좋은 총총이 (실4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(str, input().rstrip().split())) for _ in range(N)]

dance = set(["ChongChong"])
for i in range(N):
  if arr[i][0] in dance or arr[i][1] in dance:
    dance.add(arr[i][0])
    dance.add(arr[i][1])
print(len(dance))