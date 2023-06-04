# 5. I AM IRONMAN(실3)

import sys
input = sys.stdin.readline

# 입력
N, P = map(int, input().split())
W, L, G = map(int, input().split())
dic = {}
for i in range(P):
  name, wl = map(str, input().split())
  dic[name] = wl
player = [input().rstrip() for _ in range(N)]

# 계산
result = 0
f = 0
for i in range(N):
  if player[i] in dic:
    if dic[player[i]] == 'W':
      result += W
    else:
      result = max(0, result-L)
  else:
    result = max(0, result-L)
  if result >= G:
    print("I AM NOT IRONMAN!!")
    f = 1
    break
if f == 0:
  print("I AM IRONMAN!!")