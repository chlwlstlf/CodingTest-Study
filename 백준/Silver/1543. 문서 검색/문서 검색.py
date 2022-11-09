sen = input()
word = input()

result = 0

i = 0
while i < len(sen) :
  cnt = 0
  if word[0] == sen[i] :
    j = 0
    for j in range (len(word)) :
      if i+j < len(sen) and word[j] == sen[i+j] : 
        cnt += 1
  if cnt == len(word) :
    i += cnt
    result += 1
  else :
    i += 1

print(result)