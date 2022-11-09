# 14. 병든나이트(실3) 구글링+지연이 도움

N, M = map(int, input().split())

if N == 1 :
  result = 1
elif N == 2 :
  result = min(4, (M+1)//2)
elif M < 7 :
  result = min(4, M)
else :
  result = M-2

print(result)