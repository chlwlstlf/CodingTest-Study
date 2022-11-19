# 7. 숫자 카드 (실5)

import sys
input = sys.stdin.readline

#이진 탐색 함수
def binary_search(array, target, start, end):
  if start > end :
    return None
  mid = (start + end)//2
  if array[mid] == target:
    return mid
  elif array[mid] > target :
    return binary_search(array, target, start, mid-1)
  else :
    return binary_search(array, target, mid+1, end)

N = int(input())
card1 = list(map(int, input().split()))
M = int(input())
card2 = list(map(int, input().split()))

result = ''
card1.sort()
for i in range(M):
  bs = binary_search(card1, card2[i], 0, N-1)
  if bs == None :
    result += '0 '
  else :
    result += '1 '

print(result)
