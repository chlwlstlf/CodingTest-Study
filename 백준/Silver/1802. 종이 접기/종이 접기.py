import sys

T = int(sys.stdin.readline())

for i in range (T) :
  P = input()
  P = list(map(int, str(P)))

  N = 0
  length = len(P)+1
  while length > 1 :
    length /= 2
    N += 1
  
  f = 1
  for j in range (N, 0, -1) :
    n = 2**j-2
    for k in range(n//2) :
      if P[k]+P[n-k] != 1 :
        f = 0

  if f == 1 :
    print('YES')
  else :
    print('NO')