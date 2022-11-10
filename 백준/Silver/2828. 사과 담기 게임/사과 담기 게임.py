# 34. 사과 담기 게임(실5)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
J = int(input())
X = [int(input()) for _ in range(J)]

start = 1
end = M
result = 0

for i in range (J):
  if X[i] < start :
    result += start-X[i]
    end -= start-X[i]
    start -= start-X[i]
  if X[i] > end :
    result += X[i]-end
    start += X[i]-end
    end += X[i]-end
print(result)