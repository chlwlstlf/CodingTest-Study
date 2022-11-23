import sys
# input = sys.stdin.readline

N = int(input())

cnt = 0
for i in range (1, min(N+1, 1000)):
  if i < 100 :
    cnt += 1
  else :
    if (i%10 + i//100)/2 == (i%100)//10:
      cnt += 1
print(cnt)
