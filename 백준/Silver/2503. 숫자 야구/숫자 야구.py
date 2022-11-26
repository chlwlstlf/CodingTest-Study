# 16. 숫자 야구 (실3) 틀림


import sys
input = sys.stdin.readline

N = int(input())
num = []
for i in range (N):
  num.append(list(map(int, input().split())))
  num[i][0] = list(map(int,str(num[i][0])))

result = 0
for i in range (111, 1000):
  i = list(map(int,str(i)))
  if 0 in i :
    continue
  if i[0] != i[1] and i[1] != i[2] and i[2] != i[0] :
    f = 0
    for j in range (N):
      strike = 0
      ball = 0
      for k in range(3):
        if i[k] == num[j][0][k] :
          strike += 1
        if i[k] in num[j][0] and i[k] != num[j][0][k] :
          ball += 1
      if strike == num[j][1] and ball == num[j][2]:
        f += 1
    if f == N :
      result += 1
print(result)