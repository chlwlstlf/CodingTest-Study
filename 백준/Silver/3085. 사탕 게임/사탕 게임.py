# 15. 사탕 게임 (실3) 못풀겠음

import sys
import collections
input = sys.stdin.readline

N = int(input())
C = [list(input().rstrip()) for _ in range(N)]

def max_color(array):
  result = 0
  for i in range(len(array[0])):
    a = array[i]
    init = a[0]
    max_a = 0
    cnt = 1
    for j in range(1, len(array[0])):
      if a[j] == init :
        cnt += 1
      else :
        init = a[j]
        cnt = 1
      if cnt > max_a :
        max_a = cnt

    b = [c[i] for c in array]
    init = b[0]
    max_b = 0
    cnt = 1
    for j in range(1, len(array[0])):
      if b[j] == init :
        cnt += 1
      else :
        init = b[j]
        cnt = 1
      if cnt > max_b :
        max_b = cnt
    if max(max_a, max_b) > result:
      result = max(max_a, max_b)
  return result

r = []
for i in range (N):
  for j in range (N):
    if i != 0 :
      C[i][j], C[i-1][j] = C[i-1][j], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i-1][j] = C[i-1][j], C[i][j]
    if j != 0 :
      C[i][j], C[i][j-1] = C[i][j-1], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i][j-1] = C[i][j-1], C[i][j]
    if i != N-1 :
      C[i][j], C[i+1][j] = C[i+1][j], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i+1][j] = C[i+1][j], C[i][j]
    if j != N-1 :
      C[i][j], C[i][j+1] = C[i][j+1], C[i][j]
      r.append(max_color(C))
      C[i][j], C[i][j+1] = C[i][j+1], C[i][j]
print(max(r))