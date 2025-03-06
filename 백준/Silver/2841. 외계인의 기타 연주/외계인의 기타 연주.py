# 외계인의 기타 연주 (실1)

import sys
input = sys.stdin.readline

N, P = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 0
stack = [[] for _ in range(7)]

for n, p in arr:
  if not stack[n]:
    stack[n].append(p)
    answer += 1
  else:
    while stack[n] and stack[n][-1] > p:
      stack[n].pop()
      answer += 1
    if stack[n] and stack[n][-1] == p:
      continue
    stack[n].append(p)
    answer += 1
print(answer)