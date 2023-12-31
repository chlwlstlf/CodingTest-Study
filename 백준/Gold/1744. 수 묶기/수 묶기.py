# 2. 수 묶기 (골4)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = [int(input()) for _ in range(N)]

# 음수, 0, 양수 나누기
result = 0
arr.sort()
minus = []
hasZero = False
plus = []
for i in range(len(arr)):
  if arr[i] < 0:
    minus.append(arr[i])
  elif arr[i] > 0:
    if arr[i] == 1:
      result += 1
    else:
      plus.append(arr[i])
  else:
    hasZero = True

# 음수
for i in range(0, len(minus), 2):
  if i+1 < len(minus):
    result += minus[i]*minus[i+1]
# 0
if len(minus)%2 == 1 and hasZero == False:
  result += minus[-1]
# 2이상 양수
plus.sort(reverse=True)
for i in range(0, len(plus), 2):
  if i+1 < len(plus):
    result += plus[i]*plus[i+1]
if len(plus)%2 == 1:
  result += plus[-1]

# 출력
print(result)