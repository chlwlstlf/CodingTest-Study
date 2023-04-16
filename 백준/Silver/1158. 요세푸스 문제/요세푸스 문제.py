# 3. 요세푸스 문제 (실4)

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

q = deque()
for i in range(N):
  q.append(i+1)

result = '<'
idx = 0
for i in range(N):
  #K-1 명은 넘어감
  for j in range(K-1):
    q.append(q.popleft())

  #K 번째 사람 result에 넣기
  result += str(q.popleft())
  if i == N-1:
    break
  result += ', '

result += '>'
print(result)
