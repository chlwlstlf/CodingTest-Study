# 1. 균형잡힌 세상 (실4)

import sys
input = sys.stdin.readline

def isBalance(string):
  stack = []
  for s in string:
    if s in '([':
      stack.append(s)
    elif s == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        return False
    elif s == ']':
      if stack and stack[-1] == '[':
        stack.pop()
      else:
        return False
  if stack:
    return False
  return True

while True:
  string = input().rstrip()
  if string == '.':
    break
  if isBalance(string):
    print('yes')
  else:
    print('no')