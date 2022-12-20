case = []

while True :
  result = 0
  L, P, V = map(int, input().split())
  if L==0 and P==0 and V== 0 :
    break

  result += (V//P)*L
  result += L if V%P > L else V%P
  case.append(result)

i = 1
for c in case :
  print('Case %d: %d' %(i, c))
  i += 1