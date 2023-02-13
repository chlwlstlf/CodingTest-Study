import sys
input = sys.stdin.readline

key = input().rstrip()
word = input().rstrip()

#원래 배열로 만들기
code = []
start = 0
for i in range(len(word)//len(key)):
  c = []
  for j in range(len(key)):
    c.append(word[j*(len(word)//len(key))+i])
  code.append(c)

#키 순서 찾기
n = []
for i in range(len(key)):
  cnt = 0
  for j in range(len(key)):
    if key[j] < key[i]:
      cnt += 1
  if cnt in n:
    while cnt in n:
      cnt += 1
    n.append(cnt)
  else:
    n.append(cnt)

#새로운 배열에 순서바뀐 암호문 넣기
result = []
for i in range(len(word)//len(key)):
  r = []
  for j in n:
    r.append(code[i][j])
  result.append(r)

#출력
for i in range(len(word)//len(key)):
  for j in range(len(key)):
    print(result[i][j], end='')