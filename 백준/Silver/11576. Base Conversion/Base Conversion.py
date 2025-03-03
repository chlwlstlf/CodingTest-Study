# Base Conversion (실5)

import sys
input = sys.stdin.readline

A, B = map(int, input().split())
m = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(m):
  result += (A**i)*(arr[m-i-1])

answer = []
while result > 0:
  answer.append(result%B)
  result //= B

answer.reverse()
print(*answer)