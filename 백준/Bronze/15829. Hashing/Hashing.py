import sys
input = sys.stdin.readline

L = int(input())
string = input().rstrip()

def H(word, i):
  return (ord(word)-ord('a')+1)*(31**i)%1234567891

result = 0
for i in range(L):
  result += H(string[i], i)
print(result)