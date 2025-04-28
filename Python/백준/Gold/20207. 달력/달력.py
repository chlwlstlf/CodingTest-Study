# 달력 (골5)

import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x: (x[0], -x[1]))

imos = [0]*367
for a in arr:
  S, E = a[0], a[1]+1
  imos[S] += 1
  imos[E] -= 1

now = 0
for i in range(367):
  now += imos[i]
  imos[i] = now

answer = 0
width = 0
height = 0
for i in range(1, 367):
  if imos[i] > 0:
    width += 1
    height = max(height, imos[i])
  else:
    answer += width * height
    width, height = 0, 0

print(answer)
