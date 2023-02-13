import sys
input = sys.stdin.readline

while True:
  try:
    s, t = map(str, input().rstrip().split())
    j = 0
    cnt = 0
    for i in range(len(t)):
      if t[i] == s[j]:
        cnt += 1
        j += 1
      if j == len(s):
        break

    if cnt == len(s):
      print('Yes')
    else:
      print('No')

  except:
    break