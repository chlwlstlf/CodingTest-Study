data = input().split('-')
ans = 0
for i in data[0].split('+'):
    ans += int(i) # 처음 수

for i in data[1:]:
    for j in i.split('+'):
        ans -= int(j) # 이후는 다 빼준다

print(ans)