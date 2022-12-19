N, M, K = map(int, input().split())

while K > 0 :
  if N/2 >= M :
    N -= 1
    K -= 1
  else :
    M -= 1
    K -= 1
  
team = N//2 if N//2 < M else M
print(team)