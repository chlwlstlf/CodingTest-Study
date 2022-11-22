# 문자열 (실4)

A, B = input().split()

result1 = 0
result2 = len(A)
for i in range (len(B)-len(A)+1):
  cnt1 = 0
  cnt2 = 0
  for j in range (len(A)):
    if A[j] == B[i+j]:
      cnt1 += 1
    else :
      cnt2 += 1
  if cnt1 > result1 :
    result1 = cnt1
    result2 = cnt2

print(result2)