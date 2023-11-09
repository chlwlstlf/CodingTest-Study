# 3. [S/W 문제해결 기본] 1일차 - 최빈수 구하기 (D2)

from collections import Counter

T = int(input())
for i in range(T):
  idx = int(input())
  arr = list(map(int, input().split()))
  result = Counter(arr).most_common(1)[0][0]
  print(f'#{idx} {result}')