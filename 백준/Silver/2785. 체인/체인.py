import sys

N = int(input())
L = list(map(int, sys.stdin.readline().split()))
L.sort()

result = 0
while len(L) > 1 :
  if L[0] == 1 :
    del L[0]
    L.pop()
    result += 1
  else :
    L.pop()
    L[0] -= 1
    result += 1


print(result)