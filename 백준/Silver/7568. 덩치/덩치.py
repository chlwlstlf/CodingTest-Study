# 9. 덩치 (실5)

import sys
input = sys.stdin.readline

N = int(input())
person = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range (N):
  cnt = 1
  for j in range (N):
    if person[j][0]>person[i][0] and person[j][1]>person[i][1]:
      cnt += 1
  print(cnt, end=" ")