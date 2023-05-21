# 2. 한 줄로 서기 (실2)

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = [-1]*N
for i in range(N):
  cnt = 0
  for j in range(N):
    if result[j] == -1:
      if cnt == arr[i]:
        result[j] = i+1
      cnt += 1

print(*result)