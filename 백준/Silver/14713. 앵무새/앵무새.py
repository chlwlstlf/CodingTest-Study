# 10. 앵무새(실2)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
S = [deque(map(str, input().rstrip().split())) for _ in range(N)]
L = deque(map(str, input().rstrip().split()))

def isPossible():
  # L이 모두 충족되는 지
  while L:
    cnt = 0
    for j in range(N):
      if L and S[j] and L[0] == S[j][0]:
        L.popleft()
        S[j].popleft()
      else:
        cnt += 1
    if cnt == N:
      return"Impossible"
  # 앵무새가 거짓으로 말한게 없는지
  for i in range(N):
    if S[i]:
      return"Impossible"
  # 둘다 충족되면 Possible
  return"Possible"

print(isPossible())