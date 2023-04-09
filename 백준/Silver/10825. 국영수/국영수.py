# 2. 국영수 (실4)

import sys
input = sys.stdin.readline

# 입력
N = int(input())
stu = []
for i in range(N):
  stu.append(list(map(str, input().split())))
  stu[i][1:4] = map(int, stu[i][1:4])

# 정렬
stu.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

# 출력
for i in range(N):
  print(stu[i][0])
