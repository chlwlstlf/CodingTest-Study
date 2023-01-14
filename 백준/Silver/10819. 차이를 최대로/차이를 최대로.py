# 26.차이를 최대로 (실2) 틀림

import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# A.sort()

# #작은 수를 중앙에
# B = []
# B.extend([A[N-1], A[0], A[N-2]])

# #차이가 많이 나는 곳에 집어 넣는다
# for i in range(1, N-2) :
#   if abs(B[0]-A[i]) > abs(B[len(B)-1]-A[i]):
#     B.insert(0, A[i])
#   else :
#     B.append(A[i])

# #최댓값 계산
# result1 = 0
# for i in range(N-1):
#   result1 += abs(B[i]-B[i+1])


# #큰 수를 중앙에
# C = []
# C.extend([A[0], A[N-1], A[1]])

# for i in range(N-2, 1, -1) :
#   if abs(C[0]-A[i]) > abs(C[len(C)-1]-A[i]):
#     C.insert(0, A[i])
#   else :
#     C.append(A[i])

result = []

for per in list(permutations(A, N)):
  result2 = 0
  for i in range(N-1):
    result2 += abs(per[i]-per[i+1])
  result.append(result2)

print(max(result))