# 1. [S/W 문제해결 기본] 1일차 - View (D3)

for i in range(10):
  N = int(input())
  building = list(map(int, input().split()))
  result = 0
  for j in range(2, N-2):
    if building[j] > max(building[j-2], building[j-1], building[j+1], building[j+2]):
      result += building[j] - max(building[j-2], building[j-1], building[j+1], building[j+2])
  print(f'#{i+1} {result}')