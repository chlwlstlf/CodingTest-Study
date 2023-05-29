# 3. 로마 숫자 만들기 (실3)

import sys
input = sys.stdin.readline

N = int(input())

def dfs(n, cnt, ans, pre):
  global result
  if n == cnt:
    if visited[ans] == 0:
      result += 1
      visited[ans] = 13
    return
  for i in range(4):
    if arr[i] >= pre:
      dfs(n, cnt+1, ans+arr[i], arr[i])



result = 0
arr = [1, 5, 10, 50]
visited = [0]*10001
dfs(N, 0, 0, 0)
print(result)