# 괄호 끼워넣기 (실3)

import sys
input = sys.stdin.readline

S = list(input().rstrip())

stack = []
answer = 0

for s in S:
  if s == ")":
    if stack:
      stack.pop()
    else:
      answer += 1
  else:
    stack.append(s)

answer += len(stack)
print(answer)