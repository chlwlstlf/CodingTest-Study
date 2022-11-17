# 24. 회의실배정(실1) 못풀겠음

import sys
input = sys.stdin.readline

N = int(input())
C = []
for i in range (N) :
  C.append(list(map(int, input().split())))

C.sort(key = lambda x: (x[1] , x[0]))

end = C[0][1]
result = 1

for i in range (1, N) :
  if C[i][0] >= end :
    result += 1
    end = C[i][1]

print(result)




