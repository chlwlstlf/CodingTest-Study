# 28. 알바생 강호(실4)

import sys
input = sys.stdin.readline

N = int(input())
G = [int(input()) for _ in range(N)]

G.sort(reverse=True)

result = 0
for i in range(N) :
  if G[i]-i > 0 :
    result += G[i]-i

print(result)