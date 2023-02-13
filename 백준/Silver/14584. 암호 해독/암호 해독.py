import sys
input = sys.stdin.readline

code = input().rstrip()
N = int(input())
word = [input().rstrip() for _ in range(N)]

f = 0
code = list(code)

for i in range(26):
  result = ''.join(code)
  for j in range(N):
    if word[j] in result:
      f = 1
      break
  if f == 1:
    print(result)
    break
  code = list(map(lambda x:chr((ord(x)-ord('a')+1)%26+ord('a')), code))
