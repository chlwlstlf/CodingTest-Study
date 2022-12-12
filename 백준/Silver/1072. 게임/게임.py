# 19.게임 (실3) 못풀겠음

import sys
input = sys.stdin.readline

X, Y = map(int, input().split())

win = Y
Z = int(Y*100/X)

if X == Y or Z >= 99:
  print(-1)

#파라매트릭 서치
else :
  start = Y
  end = X*2
  while start <= end:
    mid = (start+end)//2
    X = (mid)-Y+X
    Y = mid
    if Z < int(Y*100/X):
      result = mid
      end = mid-1
    else:
      start = mid+1
    # print(start, end, result)
  print(result-win)




  
