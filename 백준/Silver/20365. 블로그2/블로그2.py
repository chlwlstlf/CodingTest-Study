# 31. 블로그2(실2)

N = int(input())
blog = input()

result = 1
if blog[0] == 'B' :
  r_cnt = blog.split('B')
  r_cnt = ' '.join(r_cnt).split()
  result += len(r_cnt)
if blog[0] == 'R' :
  b_cnt = blog.split('R')
  b_cnt= ' '.join(b_cnt).split()
  result += len(b_cnt)

print(result)






