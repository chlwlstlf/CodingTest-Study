# 2. 수강신청(실3)

import sys
input = sys.stdin.readline

K, L = map(int, input().split())
arr = [int(input()) for _ in range(L)]

arr.reverse()
arr = list(dict.fromkeys(arr))

for i in range(min(L, K, len(arr))):
  print(format(arr[-1-i], "08d"))
