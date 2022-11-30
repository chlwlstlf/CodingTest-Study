N = int(input())
W = [int(input()) for i in range(N)]

W.sort()
result = 0
for i in range (N) :
  if(W[i]*(N-i) >= result) :
    result = W[i]*(N-i)
print(result)