import sys

N = int(input())
S = [int(sys.stdin.readline()) for i in range(N)]

S.sort()

result = 0
for i in range(N) :
  result += abs(S[i]-(i+1))

print(result)