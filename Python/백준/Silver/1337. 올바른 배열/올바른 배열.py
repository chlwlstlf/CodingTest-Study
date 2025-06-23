# 올바른 배열 (실4)

import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

arr.sort()

start, end = 0, 0
answer = 0
while start <= end and end < N:
  if arr[end] < arr[start]+5:
    answer = max(answer, end-start+1)
    end += 1
  else:
    start += 1

print(5-answer)