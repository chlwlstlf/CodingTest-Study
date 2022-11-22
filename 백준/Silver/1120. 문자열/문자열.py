A, B = input().split()

# 알파벳 추가는 상관하지 않는다
result = len(A)
for i in range (len(B)-len(A)+1):
  cnt = 0
  for j in range (len(A)):
    if A[j] != B[i+j]:
      cnt += 1
  if cnt < result : #다른 문자가 제일 적을 때
    result = cnt

print(result)
