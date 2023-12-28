# 4. 전화번호 목록 (골4)

import sys
input = sys.stdin.readline

def isConsistency(arr):
  for i in range(len(arr)-1):
    if arr[i] == arr[i+1][:len(arr[i])]:
      return False
  return True

t = int(input())
for i in range(t):
  n = int(input())
  arr = [input().rstrip() for _ in range(n)]
  arr.sort()
  if isConsistency(arr):
    print('YES')
  else:
    print('NO')
