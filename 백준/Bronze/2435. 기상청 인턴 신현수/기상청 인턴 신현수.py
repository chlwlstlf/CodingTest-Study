# 1. 기상청 인턴 신현수 (브1)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

max_value = sum(arr[0:K])
total = sum(arr[0:K])
for i in range(1, N-K+1):
  total = total - arr[i-1] + arr[i+K-1]
  max_value = max(max_value, total)
print(max_value)