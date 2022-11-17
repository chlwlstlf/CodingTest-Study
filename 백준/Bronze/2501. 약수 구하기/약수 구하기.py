N, K = map(int, input().split())

cnt = 0
f = 0
for i in range (1, N+1):
  if N%i == 0 :
    cnt += 1
  if cnt == K:
    f = 1
    break
if f == 0 :
  print(0)
else :
  print(i)