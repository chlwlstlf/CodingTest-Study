# 4. 별 찍기 - 10 (골5)

N = int(input())

arr = [['*' for _ in range(N)] for _ in range(N)]


def star(n):
  global N
  if n == 1:
    return
  c = n//3
  for i in range(N):
    for j in range(N):
      if i%n == 0 and j%n == 0:
        for k in range(i+c, i+c*2):
          for l in range(j+c, j+c*2):
            arr[k][l] = ' '
  star(n//3)
      
star(N)

for a in arr:
  for i in a:
    print(i, end='')
  print()