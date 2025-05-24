# A를 B로 (골4)

import sys
input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
N = len(A)

def solve(A, B, N):
  # 문자 개수 같은지 검사
  alpha = [[0]*26 for _ in range(2)]
  for i in range(N):
    alpha[0][ord(A[i])-ord("A")] += 1
    alpha[1][ord(B[i])-ord("A")] += 1
  for i in range(26):
    if alpha[0][i] != alpha[1][i]:
      return -1
    
  # 뒤에서 부터 검사
  end = N-1
  start = 0
  while start <= end:
    if A[end] == B[end]:
      end -= 1
    else:
      A = A[-1] + A[:-1]
      start += 1
  return start

print(solve(A, B, N))