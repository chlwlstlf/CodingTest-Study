# 3. 주사위 쌓기(골5)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 마주보는 면
facing = [5, 3, 4, 1, 2, 0]

# 그 주사위의 최댓값 구하기
def maxDice(dice, idx):
  result = 0
  for i in range(6):
    if i != idx and i != facing[idx]:
      result = max(result, dice[i])
  return result

# 정답 구하기
answer = 0
for i in range(1, 7): # i는 첫번째 주사위의 윗면
  current = i
  total = 0
  for j in range(N):
    idx = arr[j].index(current)
    current = arr[j][facing[idx]]
    total += maxDice(arr[j], idx)
  answer = max(answer, total)
print(answer)
