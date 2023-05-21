# 3. 후위 표기식2 (실3)

import sys
input = sys.stdin.readline

N = int(input())
arr = input()
num = [int(input()) for _ in range(N)]

stack = []
for i in range(len(arr)-1):
  if arr[i] >= 'A':
    stack.append(num[int(ord(arr[i])-ord('A'))])
  else:
    n1 = stack.pop()
    n2 = stack.pop()
    if arr[i] == '+':
      stack.append(n2+n1)
    if arr[i] == '-':
      stack.append(n2-n1)
    if arr[i] == '*':
      stack.append(n2*n1)
    if arr[i] == '/':
      stack.append(n2/n1)

print(format(stack[0], ".2f"))