# 걸그룹 마스터 준석이 (실3)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

dict = {}
for _ in range(N):
  g = input().rstrip()
  dict[g] = []
  n = int(input())
  arr = [input().rstrip() for _ in range(n)]
  arr.sort()
  dict[g] = arr

for _ in range(M):
  s = input().rstrip()
  n = int(input())
  if n == 0:
    for i in range(len(dict[s])):
      print(dict[s][i])
  else:
    for key, value in dict.items():
      if s in value:
        print(key)
        break
