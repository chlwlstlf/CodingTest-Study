# 3. 수들의 합(실5)

S = int(input())

n = 1
result = 0
while True:
  result += n
  if result > S:
    break
  n += 1

print(n-1)