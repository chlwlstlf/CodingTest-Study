# 2. 추월(실1)
# 런타임 에러

import sys
input = sys.stdin.readline

# 입력
N = int(input())
front = {}
for i in range(N):
  front[input().rstrip()] = i
back = []
for i in range(N):
  back.append(front[input().rstrip()])

# 계산
result = 0
for i in range(N):
  if i in back:
    for j in range(back.index(i)):
      if back[j] > i:
        result += 1
    back = back[back.index(i):N]
print(result)