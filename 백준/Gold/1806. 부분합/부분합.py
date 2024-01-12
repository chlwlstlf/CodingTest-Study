# 2. 부분합 (골4)

import sys
input = sys.stdin.readline

# 입력
N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 초깃값
answer = N+1
start, end = 0, 0
total = 0

# 투포인터
while True:
  if total >= S:
    answer = min(answer, end-start)
    total -= arr[start]
    start += 1
  elif end == N:
    break
  else:
    total += arr[end]
    end += 1

# 출력
if answer == N+1:
  print(0)
else:
  print(answer)