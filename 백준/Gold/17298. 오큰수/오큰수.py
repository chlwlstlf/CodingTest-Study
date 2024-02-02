# 4. 오큰수 (골4) 구글링

import sys
input = sys.stdin.readline

# 입력
N = int(input())
A = list(map(int, input().split()))

answer = [-1]*N
stack = [0] #인덱스 저장하는 스택

for i in range(1, N):
  while stack and A[stack[-1]] < A[i]:
    answer[stack.pop()] = A[i]
  stack.append(i)
  
print(*answer)