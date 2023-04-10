# 3. 다음 순열 (실3)

import sys
input = sys.stdin.readline

N = int(input())
dic = list(map(int, input().split()))

asce = sorted(dic)
desc = sorted(dic, reverse=True)

if len(dic) == 1:
  print(-1)
elif dic == asce:
  dic[-1], dic[-2] = dic[-2], dic[-1]
  for i in range(N):
    print(dic[i], end =' ')
elif dic == desc:
  print(-1)
else:
  #내림차순이 끝나는 지점 찾기
  for i in range(N):
    if dic[i] > dic[i-1]:
      idx = i

  #dic[idx-1]과 dic[idx-1]보다 크면서 제일 뒤에 있는 수 위치 바꾸기
  for i in range(N-1, idx-1, -1):
    if dic[idx-1] < dic[i]:
      dic[idx-1], dic[i] = dic[i], dic[idx-1]
      break

  #dic[idx:N] 오름차순으로 바꾸기
  dic[idx:N] = sorted(dic[idx:N])

  #출력
  for i in range(N):
    print(dic[i], end=' ')



