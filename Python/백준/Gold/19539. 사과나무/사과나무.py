# 사과나무 (골5)

import sys
input = sys.stdin.readline
import copy

N = int(input())
arr = list(map(int, input().split()))

def solve(arr):
  mod = 0
  result = 0
  odd = 0
  for a in arr:
    mod += a%3
    result += a//2
    odd += a%2

  # 나머지가 3의 배수가 아니라면 바로 NO return
  if mod%3 != 0:
    return "NO"
  
  # 2의 개수 >= 1의 개수면 YES return
  if result >= odd:
    return "YES"

  return "NO"

print(solve(arr))