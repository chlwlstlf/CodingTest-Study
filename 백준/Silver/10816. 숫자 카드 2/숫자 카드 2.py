import sys
# input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

card1.sort()
for i in range(M):
  result = bisect_right(card1, card2[i])-bisect_left(card1, card2[i])
  print(result, end=' ')

