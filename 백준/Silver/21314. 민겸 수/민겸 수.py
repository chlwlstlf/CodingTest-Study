# 38. 민겸 수(실2) 틀림

import sys
input = sys.stdin.readline

num = input().rstrip()

big = ''
small = ''

m = 0
for i in range (len(num)) :
  if num[i] == 'M' :
    m += 1
  else :
    if m > 0 :
      big += str(5*(10**m))
      small += str(10**(m-1)) + '5'
    else :
      big += '5'
      small += '5'
    m = 0

if m > 0 :
  big += '1' * m
  small += str(10**(m-1))

print(big)
print(small)


    

    
