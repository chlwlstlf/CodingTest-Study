X, Y, W, S = map(int, input().split())

if (W*2 <= S) : #직선 시간 2배가 대각선 시간보다 작거나 같을 때
  print((X+Y)*W) #전부다 직선으로 계산
elif (W <= S and S < W*2): #대각선 시간이 직선 시간과 직선 시간 2배 사이일 때
  result = 0
  result += (max(X, Y) - min(X, Y))*W
  result += min(X, Y)*S
  print(result) #최대한 대각선으로 가고 나머지는 직선으로 계산
else : #대각선 시간이 직선시간보다 작을 때
  result = 0
  result += min(X, Y)*S
  if (max(X, Y) - min(X, Y))%2 == 0 :
    result += (max(X, Y) - min(X, Y))*S
  else :
    result += ((max(X, Y) - min(X, Y))-1)*S + W
  print(result) #직선 2개면 대각선으로 가기