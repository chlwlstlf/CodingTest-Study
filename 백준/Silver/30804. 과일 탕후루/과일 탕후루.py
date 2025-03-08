# 과일 탕후루 (실2)

import sys
input = sys.stdin.readline
import copy

N = int(input())
S = list(map(int, input().split()))

arr = [0]*10

answer = 0
start = 0
end = 0
while end < N:
  arr[S[end]] += 1
  while 10-arr.count(0) > 2:
    arr[S[start]] -= 1
    start += 1
  answer = max(answer, end-start+1)
  end += 1

print(answer)
