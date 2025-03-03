# 파일 정리 (실3)

import sys
input = sys.stdin.readline

N = int(input())

dict = {}
arr = []
for i in range(N):
  s = input().rstrip().split(".")
  if s[1] not in dict:
    dict[s[1]] = 1
    arr.append(s[1])
  else:
    dict[s[1]] += 1

arr.sort()
for a in arr:
  print(a, dict[a])
