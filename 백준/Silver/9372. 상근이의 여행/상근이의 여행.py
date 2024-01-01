# 5. 상근이의 여행 (실4)

import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
  # 입력 & 그래프 만들기
  N, M = map(int, input().split())
  arr = [list(map(int, input().split())) for _ in range(M)]
  print(N-1)
