# 2. 숫자고르기(골5)
# 유니온 파인드

import sys
input = sys.stdin.readline

#입력
N = int(input())
arr = [0] + [int(input()) for _ in range(N)]

#dfs
def dfs(v, start):
  if visited[v]:
    if v == start:
      return True
    return False
  
  visited[v] = 1
  if dfs(arr[v], start):
    return True # dfs가 True를 반환할 경우 사이클 존재
  return False

#답 구하기
answer = []
for i in range(1, N+1):
  visited = [0]*(N+1)
  if dfs(i, i):
    for j in range(1, N+1):
      if visited[j] == 1:
        answer.append(j)

#출력
answer = list(set(answer))
answer.sort()
print(len(answer))
for i in answer:
  print(i)
