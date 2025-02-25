# 카드놀이 (실3)

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

visited = [0]*(N+1)
visited[0] = 1

answer = 0
for i in range(N):
  if visited[arr[i]-1] == 0:
    answer += 1
  visited[arr[i]] = 1
print(answer)