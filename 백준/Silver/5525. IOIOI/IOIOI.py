import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input().rstrip()

P = 'I'+('OI'*N)

result = 0
for i in range(M-len(P)+1):
  if S[i] == 'I':
    if P == S[i:i+len(P)]:
      result += 1

print(result)
