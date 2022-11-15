# 25. 흙길 보수하기(실1) 틀림

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pool = []
for i in range(N) :
  pool.append(list(map(int, input().split())))

pool.sort()

result = 0
start = pool[0][0]
end = ((pool[0][1]-start+L-1)//L)*L + start

for i in range (N) :
  if end < pool[i][0] :
    result += (end-start+L-1)//L
    start = pool[i][0]
    end = ((pool[i][1]-start+L-1)//L)*L + start
  else :
    end = ((pool[i][1]-start+L-1)//L)*L + start

result += (end-start+L-1)//L
print(result)