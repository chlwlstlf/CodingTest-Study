# 1. NBA 농구(실3)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
team = []
time = []
for i in range(N):
  x, y = map(str, input().split())
  team.append(int(x))
  m, s = map(int, y.split(':'))
  time.append(m*60 + s)

# score 배열 만들기
s = [0, 0]
score = []
for i in range(N):
  s[team[i]-1] += 1
  if s[0] > s[1]:
    score.append(1)
  elif s[0] < s[1]:
    score.append(2)
  else:
    score.append(0)
# score: [1, 1, 1, 0, 2]

# 계산
arr = [score[0], time[0]]
result = [0, 0]
for i in range(1, N):
  if score[i-1] != score[i]:
    if score[i] == 0:
      result[score[i-1]-1] += time[i]-arr[1]
    elif score[i] == 1:
      arr[0] = 1
      arr[1] = time[i]
    else:
      arr[0] = 2
      arr[1] = time[i]

if score[-1] != 0:
  result[arr[0]-1] += 48*60 - arr[1] 

print("%s:%s" %("{:02d}".format(result[0]//60),"{:02d}".format(result[0]%60)))
print("%s:%s" %("{:02d}".format(result[1]//60),"{:02d}".format(result[1]%60)))