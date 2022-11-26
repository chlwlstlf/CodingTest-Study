import sys
from collections import Counter
  
N, M = map(int, input().split())

s = [input() for _ in range(N)]

hd = 0
result = []
for i in range (M) :
  dna = []
  for j in range(N) :
    dna.append(s[j][i])
  dna.sort()
  cnt = Counter(dna)
  result.append(cnt.most_common(1)[0][0])
  hd += N-cnt.most_common(1)[0][1]


print(''.join(s for s in result))
print(hd)