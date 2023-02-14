from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
Q = deque([i+1 for i in range(N)])

while len(Q) > 1:
  Q.popleft()
  Q.append(Q.popleft())

print(Q[0])

