# 2. 백만 장자 프로젝트 (D2)

T = int(input())

for i in range(T):
  N = int(input())
  arr = list(map(int, input().split()))
  result = 0
  max_v = arr[N-1]
  for j in range(N-2, -1, -1):
    if arr[j] <= max_v:
      result += max_v-arr[j]
    else:
      max_v = arr[j]
  print(f"#{i+1} {result}")
