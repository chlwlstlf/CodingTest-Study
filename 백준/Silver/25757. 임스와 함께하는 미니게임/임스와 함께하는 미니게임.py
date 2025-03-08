# 임스와 함께하는 미니게임 (실5)

import sys
input = sys.stdin.readline

N, O = input().rstrip().split()
N = int(N)
arr = set([input().rstrip() for _ in range(N)])

dict = {"Y": 1, "F": 2, "O": 3}

print(len(arr)//dict[O])